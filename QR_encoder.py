import qrcode
import qrcode.constants
import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
import time

dec = int(input("For scanning press 1\nFor create QR press 2\n"))

if dec==2:
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)
    data = input("Enter your data: ")
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",back_color="white")
    img.save("img.png")

if dec == 1:

    cap = cv.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    while True:
        ret,frame = cap.read()
    
        for barcode in decode(frame):
         print(barcode.data)
         myData = barcode.data.decode('utf-8')
         print(myData)
         pts = np.array([barcode.polygon],np.int32)
         cv.polylines(frame,[pts],True,(255,0,0),5)
         pts2 = barcode.rect
         cv.putText(frame,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv.imshow('In',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
         break
