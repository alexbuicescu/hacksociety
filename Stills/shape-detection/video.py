import cv2
import numpy as np

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(drawing,[cnt],0,(255,255,255),2)
        cv2.CHAIN_APPROX_SIMPLE
    return drawing
cap = cv2.VideoCapture(0)
while(True):

	ret,img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = 100
	max_thresh = 255
	cv2.imshow('original',img)
	drawing = thresh_callback(thresh)
	cv2.imshow('im',drawing)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()