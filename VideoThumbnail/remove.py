import os
from sklearn.metrics import mean_squared_error
from math import sqrt
from os.path import join
import cv2
import numpy as np
import shutil
from skimage.metrics import structural_similarity

path = os.getcwd()+"/images"
os.chdir(path)
myimages = []
dirFiles = os.listdir(os.getcwd())
fnames = sorted([fname for fname in os.listdir(os.getcwd()) if fname.endswith('.jpg')], key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].rsplit(None,1)[-1]))

for(i, image) in enumerate (fnames):
    for(i, imageCom)in enumerate (fnames):
        if image == imageCom:
            pass
        else:
            try:
                searchedImg = cv2.imread(image)
                ImgCompareGrey = cv2.imread(imageCom)
                FinalSearchedImg = cv2.cvtColor(searchedImg, cv2.COLOR_BGR2GRAY)
                FinalCompareImg = cv2.cvtColor(ImgCompareGrey, cv2.COLOR_BGR2GRAY)
                h = structural_similarity(FinalSearchedImg, FinalCompareImg)
            except:
                continue
            if h > 0.9:
                os.remove(image)
                print(image, imageCom, h)