
# import the opencv library
import cv2
from datetime import datetime
  
  
# define a video capture object
# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

count = 0
last_time = datetime.now()
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = cam.read()
        
    x = 30
    if count % x == 0:
        current_time = datetime.now()
        duration = (current_time - last_time).total_seconds()
        
        fps = x /duration
        last_time = current_time
    
        text = f'{"FPS: "} {round(fps, 2)}'
        print(text)
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    count += 1
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()