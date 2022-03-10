import cv2

img_counter = 0
myFrameNumber = 50
cap = cv2.VideoCapture("source_video/IMG_2135.MOV")

# get total number of frames
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# check for valid frame number
# set frame position
print("Frame Count: ", format(totalFrames))
cap.set(cv2.CAP_PROP_POS_FRAMES, int(totalFrames)-10)

ret, frame = cap.read()
cv2.imwrite("last_frame.jpg", frame)
cv2.imshow("last_frame", frame)


cv2.destroyAllWindows()