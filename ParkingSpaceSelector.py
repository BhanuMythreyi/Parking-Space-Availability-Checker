import cv2
import pickle

img = cv2.imread("ParkingSpaceImage.jpg")

width = 16 # The width is (x2 - x1) (difference between x coordinates) value which we obtained by trial and error method
height = 34 # The height is (y1 - y2) (difference between y coordinates) value which we obtained by trial and error method

try:
    with open("ParkingPlacesFile","rb") as f:
        positions = pickle.load(f)
except:
    positions = []


# using the function below we can create rectangular shapes for parking spaces, but for storing those shapes of parking places we use a pickle object
def mouseClick(events,x,y,falgs,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        positions.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(positions):
            u,v = pos
            if u< x <u+width and v< y <v+height:
                positions.pop(i)


    with open("ParkingPlacesFile","wb") as f:
        pickle.dump(positions,f)


while True:
    img = cv2.imread("ParkingSpaceImage.jpg")
    #cv2.rectangle(img,(164,166),(182,131),(255,0,255),1)

    for pos in positions:
            cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(0,0,255),1)
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseClick)
    if cv2.waitKey(1) == ord('q'):
        break