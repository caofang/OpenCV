import cv2
import numpy as np
from datetime import datetime

# Create a VideoCapture object
cap = cv2.VideoCapture(1)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_count = 0
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('output_video/myVideo.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 60, (frame_width, frame_height))

while (True):
    ret, frame = cap.read()

    if ret == True:
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # org
        org = (5, 50)
        # fontScale
        fontScale = 1
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        # text
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]

        text = f'{"Frame: "} {frame_count} {"Timestamp"} {current_time}'
        # Using cv2.putText() method
        image = cv2.putText(frame, text, org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        # Write the frame into the file 'output.avi'
        out.write(image)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        frame_count += 1

        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

    # When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()