# import cv2
#
#
# cams_test = 500
# for i in range(0, cams_test):
#     cap = cv2.VideoCapture(i)
#     test, frame = cap.read()
#     if test:
#         print("i : "+str(i)+" /// result: "+str(test))

import wmi
import re

c = wmi.WMI()
wql = "Select * From Win32_USBControllerDevice"
device_list = c.query(wql)
for item in device_list:
    q = item.Dependent.Caption
    # print(q)
    if q is not None and "Camera" in q:
        print(q)
