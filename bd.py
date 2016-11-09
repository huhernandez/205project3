# Standard imports
import imutils
import cv2
import numpy as np;

 
#define the webcam capture
cam = cv2.VideoCapture(0)

yeLo = (84, 81, 5)
yeHi = (255, 252, 175)
pts = deque(maxlen=args["buffer"])


while True:
	ret, frame = cam.read()
	resi= imutils.resize(frame, width=600)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	mask = cv2.inRange(hsv, yeLo, yeHi)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

# Read image
#im = cv2.imread(xxxxx, cv2.IMREAD_GRAYSCALE)
	#cv2.imshow('frame', resi)
	#if cv2.waitKey(1) & 0xFF == ord('q'):
        	
 
# Set up the detector with default parameters.
	detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
	keypoints = detector.detect(resi)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(resi, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints


	cv2.imshow("keypoints", im_with_keypoints)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()

