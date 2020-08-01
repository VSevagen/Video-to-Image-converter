import cv2
import os

path = '/home/sevagen/Desktop/Video-to-Image-converter/VideoThumbnail/images'
vidcap = cv2.VideoCapture('CometChat at Techstars Boulder 2019 Demo Day.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(os.path.join(path,str(count)+".jpg"), image) 
    return hasFrames
sec = 0
frameRate = 1
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)