import os
from sklearn.metrics import mean_squared_error
from math import sqrt
from os.path import join
import cv2
import numpy as np
import shutil

os.environ["PATH"] += os.pathsep + os.getcwd()

def getBwLittleImgs(datasetPath):
    # Find all classes paths in directory and iterate over it
    for (i, classPath) in enumerate(os.listdir(datasetPath)):

        # Construct detected directory with images from MobileNET SSD
        imgDir = join(datasetPath, classPath, "detected")
        # Construct directory to write 32x32 pix images
        bwDir = join(datasetPath, classPath, "bwdir")

        print(classPath)

        # Create bwDir patch or delete existing!
        if not os.path.exists(bwDir):
            os.makedirs(bwDir)
        else:
            shutil.rmtree(bwDir)
            os.makedirs(bwDir)

        # Iterate over all images in detected directory
        for (j, imgName) in enumerate(os.listdir(imgDir)):

            # Construct patch to single image
            imgPath = join(imgDir, imgName)
            # Read image using OpenCV as grayscale
            image = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

            # Check if we opened an image.
            if image is not None:
                # Resize opened image
                resized_image = cv2.resize(image, (32, 32))
                resized_image = np.array(resized_image)
                # Save image to bwdir. Name should be the same as name in "detected" directory
                cv2.imwrite(os.path.join(bwDir, imgName), resized_image)
            # else:
            #     # remove a file that is not an image. I don't need it.
            #     print(imgPath)
            #     os.remove(imgPath)

def findDelDuplBw(searchedName, bwDir):
        # Join path to orginal image that we are looking duplicates
        searchedImg = join(bwDir, searchedName)

        # Start iterate over all bw images
        for (j, cmpImageName) in enumerate(os.listdir(bwDir)):

            if cmpImageName == searchedName:
                # If name in bwDir is equal to searched image - pass. I don't wan to deletde searched image in bw dir
                pass
            else:
                # If name is different - concatenate path to image
                cmpImageBw = join(bwDir, cmpImageName)

                try:
                    # Open image in bwDir - The searched image
                    searchedImageBw = np.array(cv2.imread(searchedImg, cv2.IMREAD_GRAYSCALE))
                    # Open image to be compared
                    cmpImage = np.array(cv2.imread(cmpImageBw, cv2.IMREAD_GRAYSCALE))
                    # Count root mean square between both images (RMS)
                    rms = sqrt(mean_squared_error(searchedImageBw, cmpImage))
                except:
                    continue

                # If RMS is smaller than 3 - this means that images are simmilar or the same
                if rms < 3:
                    # Delete compared image in BW dir
                    os.remove(cmpImageBw)
                    print (searchedImg, cmpImageName, rms)

def findDelDetected(detectedDir, bwDir):
    # I have to compare bw dir and detected dir.
    # In bw dir I get rid of duplacates. Now I have to
    # get rid of duplicates in detected dir

    # List all bw files in bw dir
    bwFiles = os.listdir(bwDir)

    # Iterate over detected dir
    for file in os.listdir(detectedDir):
        # Check if file in detected dir can be found in bw dir
        if file not in bwFiles:
            # Deletde if not. This means that that the duplicate or simillar image is found
            print (file,  " to be deleted")
            os.remove(os.path.join(detectedDir, file))

def main():

    # Define working directory - direcotry with our dowloaded data images
    datasetPath = os.getcwd() + "/Downloads"

    # To clean data I wan to produce 32x32 pix images of data set.
    # And store them in "bwdir" in every class
    getBwLittleImgs(datasetPath)

    # Now lets iterate over all classes in data set
    for (i, classPath) in enumerate(os.listdir(datasetPath)):

        # Join detected by previous script path
        detectedDir = join(datasetPath, classPath, "detected")
        # Join black-white images path
        bwDir = join(datasetPath, classPath, "bwdir")

        # Iterate over images in one class - detected images previously by MobileSSD net
        for (i, detectedImg) in enumerate(os.listdir(detectedDir)):
            # Find duplicated BW images and delete duplicates.
            findDelDuplBw(detectedImg, bwDir)

        # Basing on cleaned BW images, now clean detected direcotry comparing data
        # between detected directory and bwDir directory
        findDelDetected(detectedDir, bwDir)

        # Remove bwDir - we don't need it any more
        shutil.rmtree(bwDir)



if __name__ == "__main__":
    main()