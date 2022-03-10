# image
# https://techtutorialsx.com/2017/05/02/python-opencv-face-detection-and-counting/
# streaming
# https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

def capture(src):
    cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)

    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('img', img)

        if cv2.waitKey(30) & 0xff == 27:
            break

    cap.release()


def still_image(src):
    image = cv2.imread(src)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    print(type(faces))

    if len(faces) == 0:
        print("No faces found")

    else:
        print(faces)
        print(faces.shape)
        print("Number of faces detected: " + str(faces.shape[0]))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

        cv2.rectangle(image, (0, image.shape[0] - 25), (270, image.shape[0]), (255, 255, 255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0, image.shape[0] - 10),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

        cv2.imshow('Image with faces', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    img_src = 'img/portugal_team.jpg'

    capture(0)
    # still_image(img_src)

    # if cv2.waitKey(30) & 0xff == 27:
    #     cv2.destroyAllWindows()

if __name__ == '__main__':
    main()