
from PyQt5 import QtWidgets , QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
import sys
import cv2
import winsound
import smtplib
from email.message import EmailMessage
import random

class Ui_SecurityCameraStart(QDialog):
    def __init__(self):
        super(Ui_SecurityCameraStart, self).__init__()
        loadUi("SecurityCameraStart.ui", self)
        self.Submit_button_Home.clicked.connect(self.gotoWidget)

    def gotoWidget(self):
        page = WidgetScreen()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class WidgetScreen(QDialog):
    def __init__(self):
        super(WidgetScreen, self).__init__()
        loadUi("SecurityCamera.ui",self)
        self.Submit_button.clicked.connect(self.function)
        self.BrowseButton.clicked.connect(self.pushButton_handler)

    def function(self):
        global email_address, email_password, msg
        email_address = "seccameraepl445@gmail.com"
        email_password = "wmmqojqunhcqxwtb"
        email = str(self.Email_lineEdit.text())
        if (len(email) == 0):
            email = "nvaki001@ucy.ac.cy"
        # create email
        msg = EmailMessage()
        msg['Subject'] = "URGENT! EPL445 Security Camera - Motion Detection"
        msg['From'] = email_address
        msg['To'] = email
        msg.set_content("Hello,\n"
                        "There is someone at your front door! \nPlease check it out.\n"
                        "\n"
                        "Your Security Camera. ")
        if self.LiveCameraRadioButton.isChecked():
            self.motion_detection(email_address,email_password,msg)

        if self.VideoFromFileRadioButton_2.isChecked():
            self.motion_detection1()

    def pushButton_handler(self):
        self.open_dialog_box()
    def open_dialog_box(self):

        filename = QFileDialog.getOpenFileName(filter="Videos (*.mp4 *.avi *.mov)")
        global path
        path = filename[0]
        self.VideoBrowseLineEdit.setText(path)

    def motion_detection(self, email, epassword, msg):
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame1 = cam.read()
            ret, frame2 = cam.read()
            diff = cv2.absdiff(frame1, frame2)  # apoliti timi (frame1 - frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email, epassword)
                for c in contours:
                    if cv2.contourArea(c) < 6000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame1, "Status: {}".format('Movement'), (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 2)
                    self.screenshot(frame1)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                    smtp.send_message(msg)
                if cv2.waitKey(10) == ord('q'):  # gia na teliosi o kodikas, o user prepei na patisei q.
                    break
                cv2.imshow('Security Camera', frame1)

    def motion_detection1(self):
        video = cv2.VideoCapture(path)
        while video.isOpened():
            ret, frame1 = video.read()
            ret, frame2 = video.read()
            diff = cv2.absdiff(frame1, frame2)  # apoliti timi (frame1 - frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
            for c in contours:
                if cv2.contourArea(c) < 6000:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame1, "Status: {}".format('Movement'), (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                self.screenshot(frame1)
            if cv2.waitKey(10) == ord('q'):  # gia na teliosi o kodikas, o user prepei na patisei q.
                break
            cv2.imshow('Security Camera', frame1)

    def screenshot (self,frame1):
        name = "suspect_image(" + str(random.random()) + ").jpg"
        cv2.imwrite(filename=name, img=frame1)


app = QApplication(sys.argv)
welcome = Ui_SecurityCameraStart()
widget = QtWidgets.QStackedWidget()
app.setObjectName("Security Camera")
widget.addWidget(welcome)
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
widget.setWindowIcon(icon)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.setWindowTitle("Security Camera EPL445")
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")


