import cv2
import sys

#cascPath = sys.argv[1]


video_capture = cv2.VideoCapture(0)
x=5;
xx=150;
y=350;
yy=400;
x1=170;
xx1=310;
y1=400;
yy1=480;
x2=320;
xx2=445;
x3=465;
xx3=620;

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    # Draw a rectangles on the screen
    
    cv2.rectangle(frame, (x, y), (xx, yy), (255,0 , 0), 2)
    cv2.rectangle(frame, (x1, y1), (xx1, yy1), (0, 255, 0), 2)
    cv2.rectangle(frame, (x2, y1), (xx2, yy1), (0, 255, 0), 2)
    cv2.rectangle(frame, (x3, y), (xx3, yy), (255, 0, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
