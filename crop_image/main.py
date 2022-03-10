import cv2


def crop(src, dest, x,y,w,h):

    img = cv2.imread(src)
    # crop_img = img[0:1200, 1920:1920 + 1920]
    crop_img = img[y:y+h , x:x + w]
    cv2.imshow("cropped", crop_img)
    cv2.imwrite(dest,crop_img)
    cv2.waitKey(1)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    "images/Screenshot (3).png"

    for x in range(3, 22):
        crop("images/Screenshot ({id}).png".format(id=x), "images/screenshot_{id}.png".format(id=x), 1920, 0, 1920, 1200)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
