import os
from sklearn.metrics import mean_squared_error
from math import sqrt
from os.path import join
import cv2
import numpy as np
import shutil

def getGreyImgs(Path, greyDir):
    for(j, imgName) in enumerate(os.listdir(Path)):
        imagePath = join(Path, imgName)

        # Convert the image to greyscale
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE) 

        # Resize image to 32x32 and store them in greyDir
        if image is not None:
            resizeImage = cv2.resize(image, (32, 32))
            resizeImage = np.array(resizeImage)
            cv2.imwrite(os.path.join(greyDir, imgName), resizeImage)

def FindNRemoveGreyDupli(greyDir):
    for(i, greyImg) in enumerate(os.listdir(greyDir)):
        # Take first image for comparing
        searchedImg = join(greyDir, greyImg)

        for(j, ImgCompare) in enumerate(os.listdir(greyDir)):
            # Check whether we are comparing same image as above. In that
            # case, we skip it.
            if ImgCompare == greyImg:
                pass
            else:
                ImgCompareGrey = join(greyDir, ImgCompare)
                try:
                    # 
                    FinalSearchedImg = np.array(cv2.imread(searchedImg, cv2.IMREAD_GRAYSCALE))
                    FinalCompareImg = np.array(cv2.imread(ImgCompareGrey, cv2.IMREAD_GRAYSCALE))
                    # rms = sqrt(mean_squared_error(FinalSearchedImg, FinalCompareImg ))
                    h = np.sum((FinalSearchedImg.astype("float") - FinalCompareImg.astype("float")) ** 2)
                    h /= float(FinalSearchedImg.shape[0] * FinalSearchedImg.shape[1])
                except:
                    continue
                if h < 500:
                    os.remove(ImgCompareGrey)
                    print (searchedImg, ImgCompareGrey, h)  

def RemoveDupli(greyDir, Path):
    greyImg = os.listdir(greyDir)

    for img in os.listdir(Path):
        if img not in greyImg and img != 'greyImg':
            os.remove(os.path.join(Path, img))

def main():
    Path = os.getcwd() + "/images"
    greyDir = join(Path, "greyImg")
    os.makedirs(greyDir)

    # Function to grey out the images and store them in greyDir
    getGreyImgs(Path, greyDir)
    FindNRemoveGreyDupli(greyDir)
    RemoveDupli(greyDir, Path)

    shutil.rmtree(greyDir)


if __name__ == "__main__":
    main()