# Program To Read video
# and Extract Frames
# https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/

import cv2
import os
from pathlib import Path
import re
import os.path

def ClearDir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))

# Function to extract frames
def FrameCapture(path):
    # Path to video file
    # vidObj = cv2.VideoCapture(path)
    capture = cv2.VideoCapture('output_video/myVideo.avi')
    fps = capture.get(cv2.CAP_PROP_FPS)
    ClearDir("video_frames")
    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1
    while success:
        # vidObj object calls read
        # function extract frames
        success, image = capture.read()
        if not success:
            continue
        # Saves the frames with frame-count

        # timestamp = capture.get(cv2.CAP_PROP_POS_MSEC)
        img_output = f'video_frames\\opencv_frame_{str(count)}.png'

        cv2.imwrite(img_output, image)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    video_dir = Path(os.getcwd(), "myVideo.avi")
    # print(video_dir)

    FrameCapture(video_dir)