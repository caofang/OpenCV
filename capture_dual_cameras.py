import argparse
from datetime import datetime
from time import sleep
import platform
import numpy as np

import cv2

def make_1080p(capture):
    capture.set(3, 1920)
    capture.set(4, 1080)

def make_720p(capture):
    capture.set(3, 1280)
    capture.set(4, 720)

def make_480p(capture):
    capture.set(3, 640)
    capture.set(4, 480)

def set_resolution(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)



def run_app(camera_index1, camera_index2, fps):
    if platform.system() == "Windows":
        cam1 = cv2.VideoCapture(camera_index1, cv2.CAP_DSHOW)
        cam2 = cv2.VideoCapture(camera_index2, cv2.CAP_DSHOW)
    if platform.system() == "Linux":
        cam1 = cv2.VideoCapture(camera_index1)
        cam2 = cv2.VideoCapture(camera_index2)
        
            
    cam1.set(cv2.CAP_PROP_FPS, fps)
    cam2.set(cv2.CAP_PROP_FPS, fps)
    # cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cam1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cam2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    
    make_720p(cam1)
    make_720p(cam2)
    # set_resolution(cam,640,480)
    # cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    img_counter = 0
    count = 0
    fps = 0.0
    last_time = datetime.now()
    sleep(1)

    if (cam1.isOpened()== False or cam1.isOpened()== False):
        print("Error opening video stream or file")


    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (5, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    
    text = f'{"FPS: "} {round(fps, 2)}'
            

    while (True):
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()
        current_time = datetime.now()
        # current_time_str = current_time.strftime('%H:%M:%S.%f')[:-3]

        # fps
        x = 30
        if count % x == 0:
            duration = (current_time - last_time).total_seconds()
            
            fps = x /duration
            last_time = current_time
        
            text = f'{"FPS: "} {round(fps, 2)}'
            print(text)
        

        image1 = cv2.putText(frame1, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        iamge2 = cv2.flip(frame2, 1)
        combined_image = np.hstack((image1, iamge2))
        
        
        cv2.imshow("test", combined_image)
        
        count += 1

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == ord(' '):
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, combined_image)
            print("{} written!".format(img_name))
            img_counter += 1

        

    cam1.release()
    cam2.release()

    cv2.destroyAllWindows()
    

# Driver Code
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c1', type=int, help='Index of which video source to use. ', default = 0)
    parser.add_argument('-c2', type=int, help='Index of which video source to use. ', default = 2)
    parser.add_argument('-f', type=int, help='FPS', default = 30)
    args = parser.parse_args()

    run_app(args.c1, args.c2, args.f)

