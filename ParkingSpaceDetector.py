import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("ParkingSpaceVideoFootage.mp4")

with open("ParkingPlacesFile","rb") as f:
    positions = pickle.load(f)

width = 16
height = 34

def AvailabilityDetector(imgPro):
    vacancy =0
    var = 0
    for pos in positions:
        i,j = pos
        imgCrop = imgPro[j:j+height,i:i+width]
        var += 1
        count = cv2.countNonZero(imgCrop)

        if count<95:
            color = (0,255,0)
            thickness = 3
            vacancy += 1
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickness)
        cv2.putText(img,str(count),(i,j+height-1), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0),1, cv2.LINE_AA,False)
    cv2.putText(img,f'Vacant_Spaces:{vacancy}/{len(positions)}',(70,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),4, cv2.LINE_AA)

    # (70,340)

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)  # This is just a loop basically, If we are done with all the frames available in the video, we reset the frame to 0 hence the video autoplays endlessly as we are working with a video of limited time period, however if this is used for a webcam then no need of this line as webcam captures continuously

    success , img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imagemedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imagemedian,kernel,iterations = 1)

    AvailabilityDetector(imgDilate)

    # for pos in positions:
    #     cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),1)
    cv2.imshow("Image",img)
    # cv2.imshow("BlurredImage",imgBlur)
    # cv2.imshow("ThresholdImage",imgThreshold)
    # cv2.imshow("medianImage",imagemedian)
    if cv2.waitKey(20) == ord('q'):
        break