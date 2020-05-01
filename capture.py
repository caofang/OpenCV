import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 2)
args = parser.parse_args()

cam = cv2.VideoCapture(args.camera_idx)

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
