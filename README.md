# Video-to-Image-converter
Passing a video as input, we generate thumbnails for every 1 sec interval of the video. The FrameRate can be adjusted in order to obtain more thumbnails. I'm using OpenCV to extract the images and in order to remove the duplicates, I'm using a structural similarity index(SSIM) to differentiate between duplicates and similar images.

<h2>Run the Program</h2>
<span>Step 1: Clone the project</span><br>
<span>Step2: Place the video you want to experiment on in the VideoThumbnail directory</span>
<span>Step3: Run <strong>python3 main.py</strong></span>

<h3>Note</h3>
<span>At the moment, SSIM is set to 0.8 or more. That is, if the difference between 2 images is more than 0.8, then they are most probably very similar. This value can be modified to suit the need of the user. Moreover, frameRate can be modified as well to either increase or decrease the number of thumbnails</span>