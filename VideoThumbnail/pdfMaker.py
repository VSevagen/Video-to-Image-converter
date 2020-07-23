import img2pdf
import os

path = os.getcwd()+"/images"
os.chdir(path)
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]))

imgDir = os.listdir(path)
for image in imgDir:
    if image.endswith(".jpg"):
        os.remove(os.path.join(path, image))
