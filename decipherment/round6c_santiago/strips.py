"""Cut readable strips/crops from the renders. Detail image = depth high-pass (~1.5 mm)
combined with two raking lights; no texture involved."""
import sys, numpy as np
from PIL import Image
from scipy import ndimage
Image.MAX_IMAGE_PIXELS = None

def load(d, face):
    g = lambda n: np.asarray(Image.open(f"{d}/{face}_{n}.png").convert("L")).astype(float)
    return g

def detail(d, face, box, rot180=False, scale=1.0):
    x0, y0, x1, y1 = box
    g = load(d, face)
    a = g("rake135")[y0:y1, x0:x1]; b = g("rake045")[y0:y1, x0:x1]; r = g("relief")[y0:y1, x0:x1]
    hp = r - ndimage.gaussian_filter(r, 20)
    def n(z):
        p0, p1 = np.percentile(z, [1, 99]); return np.clip((z - p0) / max(p1 - p0, 1e-6), 0, 1)
    out = {"rake135": n(a), "rake045": n(b), "relief_hp": n(hp), "combo": n(0.4 * n(a) + 0.3 * n(b) + 0.6 * n(hp))}
    import cv2
    cl = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    hp2 = r - ndimage.gaussian_filter(r, 12)
    out["incised"] = cl.apply((n(ndimage.gaussian_filter(hp2, 1.0)) * 255).astype(np.uint8)) / 255.0
    out["combo"] = cl.apply((out["combo"] * 255).astype(np.uint8)) / 255.0
    res = {}
    for k, v in out.items():
        im = Image.fromarray((v * 255).astype(np.uint8))
        if rot180: im = im.rotate(180)
        if scale != 1.0: im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        res[k] = im
    return res
