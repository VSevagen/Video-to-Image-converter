import numpy as np
import cv2
import os
from os.path import join
# from matplotlib import pyplot as plt

path = os.getcwd()+"/images"
os.chdir(path)
width = int(input("Enter the width of face: "))
height = int(input("Enter the height of face: "))
point = (width, height)
for(i, image) in enumerate(os.listdir(path)):
    Image = cv2.imread(image)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    test_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    
    haar_cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
    faces_rects = haar_cascade_face.detectMultiScale(test_image, scaleFactor = 1.1, minNeighbors = 5, minSize = point)
    if len(faces_rects) >= 1:
        os.remove(os.path.join(path, image))
os.chdir("..")

# for (x,y,w,h) in faces_rects:
#     cv2.rectangle(Image,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = Image[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# cv2.imshow('img',Image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # cv2.waitKey(1)

