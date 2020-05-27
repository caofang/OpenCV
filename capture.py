import argparse
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

parser = argparse.ArgumentParser()
parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
args = parser.parse_args()

cam = cv2.VideoCapture(args.camera_idx)
# set_resolution(cam, 960, 540)
make_480p(cam)

# cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

img_counter = 0

# while True:
while (cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
