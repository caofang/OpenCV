import argparse
from datetime import datetime
from time import sleep
import platform

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



def run_app(camera_index, fps):
    if platform.system() == "Windows":
        cam = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)        
    if platform.system() == "Linux":
        cam = cv2.VideoCapture(camera_index)
        
            
    cam.set(cv2.CAP_PROP_FPS, fps)
    # cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    
    make_720p(cam)
    # set_resolution(cam,640,480)
    # cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    print("== FPS: ", cam.get(cv2.CAP_PROP_FPS))


    img_counter = 0
    count = 0
    fps = 0.0
    last_time = datetime.now()
    sleep(1)

    if (cam.isOpened()== False):
        print("Error opening video stream or file")


    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (5, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    
    text = f'{"FPS: "} {round(fps, 2)}'
            

    while (True):
        ret, frame = cam.read()        

        x = 10
        if count % x == 0:
            current_time = datetime.now()            
            duration = (current_time - last_time).total_seconds()
            
            fps = x /duration
            last_time = current_time
        
            text = f'{"FPS: "} {round(fps, 2)}'
            # print(text)
        

        image = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("test", image)
        
        count += 1

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == ord(' '):
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1        

    cam.release()
    cv2.destroyAllWindows()
    

# Driver Code
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int, help='Index of which video source to use. ', default = 0)
    parser.add_argument('-f', type=int, help='FPS', default = 30)
    args = parser.parse_args()

    run_app(args.c, args.f)