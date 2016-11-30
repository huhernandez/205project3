# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import pygame
import pyaudio
import wave
import pyglet

x=5
xx=150
y=350
yy=400
x1=170
xx1=310
y1=400
yy1=480
x2=320
xx2=445
x3=465
xx3=620
pts=[]

s = pyglet.resource.media('808-Clap12.wav')

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
video_capture = cv2.VideoCapture(0)

while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()
	# Draw a rectangles on the screen
	print x
	print y
	print xx
	print yy

	cv2.rectangle(frame, (x, y), (xx, yy), (255,0 , 0), 2)
	cv2.rectangle(frame, (x1, y1), (xx1, yy1), (0, 255, 0), 2)
	cv2.rectangle(frame, (x2, y1), (xx2, yy1), (0, 255, 0), 2)
	cv2.rectangle(frame, (x3, y), (xx3, yy), (255, 0, 0), 2)
	# Display the resulting frame
	#cv2.imshow('Video', frame)


	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = (0,0)
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((a, b), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(a), int(b)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
	print center
	xax, yax = center


	#Left Drumstick

	

	


	if xax > x and xax < xx:
		if yax > y and yax < yy:
			s.play()
			print "yo"
	if xax > x1 and xax < xx1:
		if yax > y1 and yax < yy1:
			s.play()
			print "yo2"
	if xax > x2 and xax < xx2:
		if yax > y1 and yax < yy1:
			s.play()
			print "yo3"
	if xax > x3 and xax < xx3:
		if yax > y and yax < yy:
			s.play()
			print "yo4"
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	 
# cleanup the camera and close any open windows
video_capture.release()
cv2.destroyAllWindows()
