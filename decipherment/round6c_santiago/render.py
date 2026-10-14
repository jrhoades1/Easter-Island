"""Headless orthographic / cylindrical renders of the MNHN Santiago 3D models.

Ray-casts the mesh (trimesh + embree) on a regular grid, so every output pixel
has a measured depth, an interpolated surface normal and a texture sample.
Outputs per view: texture, relief (depth minus a broad blur), mesh-normal shading
with no texture, and raking light from several azimuths.

Usage: python render.py MODEL_DIR OUT_DIR --mode {slab,cylinder} --px LONG_PIXELS
Raw models are NOT part of the repository (MNHN; see docs).
"""
import argparse, glob, json, os
import numpy as np, trimesh
from PIL import Image
from scipy import ndimage
Image.MAX_IMAGE_PIXELS = None


def load(model_dir):
    obj = (glob.glob(os.path.join(model_dir, "unz", "*.obj")) + glob.glob(os.path.join(model_dir, "unz", "*.OBJ")))[0]
    m = trimesh.load(obj, process=False, force="mesh")
    tex = sorted(glob.glob(os.path.join(model_dir, "textures", "*")))[0]
    img = np.asarray(Image.open(tex).convert("RGB"))
    uv = m.visual.uv if hasattr(m.visual, "uv") and m.visual.uv is not None else None
    return m, uv, img


def pca_frame(m):
    v = m.vertices - m.vertices.mean(0)
    _, _, vt = np.linalg.svd(v[:: max(1, len(v) // 50000)], full_matrices=False)
    R = vt  # rows: long, mid, thin
    if np.linalg.det(R) < 0:
        R[2] *= -1
    return m.vertices.mean(0), R


def shade(normals, mask, az_deg, el_deg):
    az, el = np.radians(az_deg), np.radians(el_deg)
    L = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
    s = np.clip((normals * L).sum(-1), 0, 1)
    s[~mask] = 0
    return s


def to8(a, mask=None, lo=1, hi=99):
    vals = a[mask] if mask is not None else a.ravel()
    if vals.size == 0:
        return np.zeros(a.shape, np.uint8)
    p0, p1 = np.percentile(vals, [lo, hi])
    out = np.clip((a - p0) / max(p1 - p0, 1e-9), 0, 1)
    if mask is not None:
        out[~mask] = 0
    return (out * 255).astype(np.uint8)


def cast(m, origins, dirs):
    loc, ray, tri = m.ray.intersects_location(origins, dirs, multiple_hits=False)
    return loc, ray, tri


def sample(m, uv, img, loc, tri):
    bary = trimesh.triangles.points_to_barycentric(m.triangles[tri], loc)
    f = m.faces[tri]
    vn = m.vertex_normals[f]
    n = (vn * bary[:, :, None]).sum(1)
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    col = None
    if uv is not None:
        t = (uv[f] * bary[:, :, None]).sum(1)
        h, w = img.shape[:2]
        x = np.clip((t[:, 0] % 1.0) * (w - 1), 0, w - 1).astype(int)
        y = np.clip((1 - (t[:, 1] % 1.0)) * (h - 1), 0, h - 1).astype(int)
        col = img[y, x]
    return n, col


def finish(out, name, depth, normals, col, mask, px_mm, meta):
    os.makedirs(out, exist_ok=True)
    H, W = mask.shape
    # relief: depth relative to a broad local surface (~8 mm), positive = raised
    sigma = max(2.0, 8.0 * px_mm)
    d = np.where(mask, depth, 0.0)
    w = ndimage.gaussian_filter(mask.astype(float), sigma)
    base = ndimage.gaussian_filter(d, sigma) / np.maximum(w, 1e-6)
    relief = np.where(mask, depth - base, 0)
    np.save(f"{out}/{name}_relief.npy", relief.astype(np.float32))
    Image.fromarray(to8(relief, mask)).save(f"{out}/{name}_relief.png")
    # normals from depth-map gradients (finer than mesh normals at grid res)
    gy, gx = np.gradient(ndimage.gaussian_filter(d, 0.7) * px_mm)
    nd = np.dstack([-gx, -gy, np.ones_like(gx)])
    nd /= np.linalg.norm(nd, axis=2, keepdims=True)
    nd[~mask] = 0
    Image.fromarray(to8(shade(nd, mask, 0, 90), mask)).save(f"{out}/{name}_normalshade.png")
    for az in (0, 90, 180, 270, 45, 135):
        Image.fromarray(to8(shade(nd, mask, az, 15), mask, 0.5, 99.5)).save(f"{out}/{name}_rake{az:03d}.png")
    if col is not None:
        Image.fromarray(col).save(f"{out}/{name}_texture.png")
    meta[name] = {"width": W, "height": H, "px_per_mm_or_unit": px_mm, "coverage": float(mask.mean())}


def slab(m, uv, img, out, long_px):
    c, R = pca_frame(m)
    v = (m.vertices - c) @ R.T
    mm = trimesh.Trimesh(v, m.faces, process=False)
    lo, hi = v.min(0), v.max(0)
    px = long_px / (hi[0] - lo[0])
    W = long_px
    H = int(np.ceil((hi[1] - lo[1]) * px))
    xs = lo[0] + (np.arange(W) + 0.5) / px
    ys = hi[1] - (np.arange(H) + 0.5) / px
    X, Y = np.meshgrid(xs, ys)
    meta = {"frame_center": c.tolist(), "frame_R": R.tolist(), "extent_units": (hi - lo).tolist()}
    for side, sgn in (("faceA", 1), ("faceB", -1)):
        # faceB viewed from the other side: mirror x so it reads unmirrored
        Xs = X if sgn == 1 else -X[:, ::-1] * -1
        o = np.stack([X.ravel(), Y.ravel(), np.full(X.size, sgn * (hi[2] + 10 if sgn == 1 else -lo[2] + 10))], 1)
        dvec = np.tile([0, 0, -sgn], (X.size, 1)).astype(float)
        depth = np.full(X.size, np.nan); N = np.zeros((X.size, 3)); C = np.zeros((X.size, 3), np.uint8)
        for s in range(0, X.size, 2_000_000):
            loc, ray, tri = cast(mm, o[s:s + 2_000_000], dvec[s:s + 2_000_000])
            n, col = sample(mm, uv, img, loc, tri)
            ray = ray + s
            depth[ray] = sgn * loc[:, 2]
            n[:, 2] *= sgn; n[:, 0] *= sgn
            N[ray] = n
            if col is not None: C[ray] = col
        mask = ~np.isnan(depth)
        depth = np.nan_to_num(depth).reshape(H, W); N = N.reshape(H, W, 3); C = C.reshape(H, W, 3)
        mask = mask.reshape(H, W)
        if sgn == -1:  # mirror so the back face reads as seen from behind
            depth, N, C, mask = depth[:, ::-1], N[:, ::-1], C[:, ::-1], mask[:, ::-1]
        finish(out, side, depth, N, C if uv is not None else None, mask, px, meta)
    return meta


def cylinder(m, uv, img, out, long_px):
    c, R = pca_frame(m)
    v = (m.vertices - c) @ R.T
    mm = trimesh.Trimesh(v, m.faces, process=False)
    lo, hi = v.min(0), v.max(0)
    px = long_px / (hi[0] - lo[0])
    rmax = np.sqrt((v[:, 1:] ** 2).sum(1)).max()
    # radius estimated as median; circumference sets angular sampling
    rmed = np.median(np.sqrt((v[:, 1:] ** 2).sum(1)))
    Wth = int(np.ceil(2 * np.pi * rmed * px))
    meta = {"frame_center": c.tolist(), "frame_R": R.tolist(), "extent_units": (hi - lo).tolist(), "r_median": float(rmed)}
    nseg = 4
    seg = long_px // nseg
    for k in range(nseg):
        xs = lo[0] + (np.arange(k * seg, (k + 1) * seg) + 0.5) / px
        th = (np.arange(Wth) + 0.5) / Wth * 2 * np.pi
        TH, X = np.meshgrid(th, xs)  # rows = along axis
        ox = X.ravel(); dy = np.cos(TH.ravel()); dz = np.sin(TH.ravel())
        o = np.stack([ox, dy * (rmax + 5), dz * (rmax + 5)], 1)
        dvec = np.stack([np.zeros_like(ox), -dy, -dz], 1)
        depth = np.full(ox.size, np.nan); N = np.zeros((ox.size, 3)); C = np.zeros((ox.size, 3), np.uint8)
        for s in range(0, ox.size, 2_000_000):
            loc, ray, tri = cast(mm, o[s:s + 2_000_000], dvec[s:s + 2_000_000])
            n, col = sample(mm, uv, img, loc, tri)
            ray = ray + s
            depth[ray] = np.sqrt(loc[:, 1] ** 2 + loc[:, 2] ** 2)
            if col is not None: C[ray] = col
        mask = ~np.isnan(depth)
        sh = TH.shape
        # transpose so the axis runs horizontally (lines of signs run along the staff)
        depth = np.nan_to_num(depth).reshape(sh).T; C = C.reshape(sh + (3,)).transpose(1, 0, 2); mask = mask.reshape(sh).T
        finish(out, f"seg{k}", depth, None, C, mask, px, meta)
    return meta


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir"); ap.add_argument("out"); ap.add_argument("--mode", default="slab"); ap.add_argument("--px", type=int, default=4000)
    a = ap.parse_args()
    m, uv, img = load(a.model_dir)
    meta = (slab if a.mode == "slab" else cylinder)(m, uv, img, a.out, a.px)
    meta.update(model=a.model_dir, faces=int(len(m.faces)), vertices=int(len(m.vertices)), texture_shape=list(img.shape))
    json.dump(meta, open(os.path.join(a.out, "render_meta.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in meta.items() if k not in ("frame_R",)}, default=str)[:800])
