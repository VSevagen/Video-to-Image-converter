import img2pdf
import os
import numpy as np

path = os.getcwd()+"/images"
os.chdir(path)
myimages = []
dirFiles = os.listdir(os.getcwd())
fnames = sorted([fname for fname in os.listdir(os.getcwd()) if fname.endswith('.jpg')], key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].rsplit(None,1)[-1]))

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in fnames if i.endswith(".jpg")]))

imgDir = os.listdir(path)
for image in imgDir:
    if image.endswith(".jpg"):
        os.remove(os.path.join(path, image))
