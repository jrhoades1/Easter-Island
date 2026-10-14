"""Straighten curved lines of signs and cut one strip per line.
Per-column-block vertical shift by cross-correlating row 'ink' profiles with the
central block (chained outward); then gaps between lines = minima of ink profile."""
import sys, os, json, numpy as np, cv2
from PIL import Image
from scipy import ndimage, signal
Image.MAX_IMAGE_PIXELS = None

def incised(d, face):
    p = f"{d}/{face}_relief.npy"
    if os.path.exists(p):
        r = np.load(p).astype(float); m = r != 0
    else:
        r = np.asarray(Image.open(f"{d}/{face}_relief.png").convert("L")).astype(float); m = r > 0
    hp = r - ndimage.gaussian_filter(r, 12)
    hp = ndimage.gaussian_filter(hp, 2.0)
    me = ndimage.binary_erosion(m, iterations=40)
    hp = np.where(me, hp, 0)
    loc = np.sqrt(ndimage.gaussian_filter(hp ** 2, 60)) + 1e-6
    hn = hp / loc
    z = np.clip(0.5 + hn / 5.0, 0, 1)
    z = cv2.createCLAHE(3.0, (16, 16)).apply((z * 255).astype(np.uint8))
    z[~m] = 255
    return z, m

def shifts(z, m, blk=150, maxs=60):
    H, W = z.shape
    ink = 255.0 - z
    nb = W // blk
    prof = [ndimage.gaussian_filter1d(ink[:, i*blk:(i+1)*blk].mean(1), 3) for i in range(nb)]
    sh = np.zeros(nb); c = nb // 2
    for direction in (1, -1):
        i = c
        while 0 <= i + direction < nb:
            a, b = prof[i] - prof[i].mean(), prof[i+direction] - prof[i+direction].mean()
            cc = [np.dot(np.roll(b, -s), a) for s in range(-maxs//3, maxs//3 + 1)]
            sh[i+direction] = sh[i] + (np.argmax(cc) - maxs//3)
            i += direction
    xs = (np.arange(nb) + 0.5) * blk
    return np.interp(np.arange(W), xs, ndimage.gaussian_filter1d(sh, 1.5))

def straighten(img, s):
    H, W = img.shape[:2]
    Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
    return cv2.remap(img, X, (Y + s[None, :]).astype(np.float32), cv2.INTER_LINEAR, borderValue=255)

if __name__ == "__main__":
    d, face, out = sys.argv[1:4]
    z, m = incised(d, face)
    s = shifts(z, m)
    zs = straighten(z, s)
    np.save(f"{out}/{face}_shift.npy", s)
    Image.fromarray(zs).save(f"{out}/{face}_incised_straight.png")
    ink = ndimage.gaussian_filter1d((255.0 - zs[:, int(zs.shape[1]*.2):int(zs.shape[1]*.8)]).mean(1), 6)
    mins, _ = signal.find_peaks(-ink, distance=80, prominence=2)
    print(json.dumps({"gaps": mins.tolist()}))
