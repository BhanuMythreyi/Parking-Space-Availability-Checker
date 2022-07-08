# Parking-Space-Availability-Checker

This is an application that can be used to determine the number of parking bays available for a vehicle that is going to enter the parking lot.

Parking Space Selector:
First I just collected an image of the parking lot from the video available. Now the size of each and every parking bay will be equal so have drawn rectangular boxes for representing the bays. The rectangular boxes on the image were drawn using mouse click events. And the boxes drawn for the parking space are stored in a pickle object using the dump function.

Parking Space Detector:
	Now The main idea used in Image Processing is that first the whole video is made into black and white, then we can observe only two colored pixels either black or white. So the basic idea is that when the cars will be present in the parking bays that’s the rectangles that we have drawn then the pixels will be white in colour and if no object is present then the pixels will be in black colour. So by setting some limit for the white pixels that can be present in the parking bay we can identify whether there is a vehicle in the bay or not. If not then the number of parking spaces available will be incremented and yeah if at all some other vehicle comes then the white pixel count in the bay increases and the total parking space count will decrease.


Required to install: new version of pip 

PIP is a package management system used to install and manage software packages/libraries written in Python. These files are stored in a large “on-line repository” termed as Python Package Index (PyPI).

pip uses PyPI as the default source for packages and their dependencies. So whenever we type:
pip install package_name
pip will look for that package on PyPI and if found, it will download and install the package on the local system.

OpenCV is an open-source computer vision library that provides privileges to play with different images and video streams and also helps in end-to-end projects like object detection, face detection, object tracking, etc.

![Coordinate Axis and rectangular boxes](https://user-images.githubusercontent.com/82871294/177572488-4cb7d8f0-4bf0-48cc-8bb6-e277ea8925db.PNG)

The width and height of the rectangular boxes drawn on the image for parking space is found by trial and error method, By changing the values of the x and y coordinates we can do that in the method cv2.rectangle(image,start_point,end_point,color,thickness) i.e. cv2.rectangle(image,(x1,y1),(x2,y2),color,thickness)
Color coordinates will be (B,G,R) where B - Blue, G - Green, R - Red; variation in the number of the different colors among B,G,R gives us a new color
For example if we want Blue color we give (255,0,0) where the first coordinate is for blue and the remaining are 0. But if we want some other color like purple we give (255,0,255), that is the combination of Blue and Red colors.
