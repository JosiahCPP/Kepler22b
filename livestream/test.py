# import the opencv library
import cv2
import numpy as np


cap = cv2.VideoCapture('http://000.00.00.0:8000/stream.mjpg')
 while(True):
    
   # Capture the video frame
   # by frame
   ret, frame = cap.read()
    # Display the resulting frame
   cv2.imshow('frame', frame)
    
   # the 'q' button is set as the
   # quitting button you may use any
   # desired button of your choice
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
 # After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
