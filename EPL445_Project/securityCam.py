import cv2
import winsound
import smtplib
from email.message import EmailMessage
import pyautogui
import numpy as np
import random


def screenshot():
    img = pyautogui.screenshot()
    name = "suspect_image(" + str(random.random()) + ").jpg"
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(filename=name, img=frame)


def motion_detection(email, epassword, msg):
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2) # apoliti timi (frame1 - frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        for c in contours:
            if cv2.contourArea(c) < 10000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
            screenshot()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email, epassword)
                smtp.send_message(msg)
        if cv2.waitKey(10) == ord('q'): #gia na teliosi o kodikas, o user prepei na patisei q.
            break
        cv2.imshow('Security Camera', frame1)


email_address = "seccameraepl445@gmail.com"
email_password = "wmmqojqunhcqxwtb"
# create email
msg = EmailMessage()
msg['Subject'] = "EPL445 Security Camera - Motion Detection"
msg['From'] = email_address
msg['To'] = "nvaki001@ucy.ac.cy"
msg.set_content("Hello, \n"
                "There is someone at your front door! \nPlease check it out.\n"
                "\n"
                "Your Security Camera. ")

motion_detection(email_address, email_password, msg)
