# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys


from matplotlib import pyplot as plt


class Ui_BrowseVideo(object):
    def setupUi(self, BrowseVideo):
        BrowseVideo.setObjectName("BrowseVideo")
        BrowseVideo.resize(554, 266)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        BrowseVideo.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FiltrService_icons_filmedvideo_280.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BrowseVideo.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(BrowseVideo)
        self.label.setGeometry(QtCore.QRect(40, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BrowseVideo)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(BrowseVideo)
        self.widget.setGeometry(QtCore.QRect(40, 80, 481, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget1 = QtWidgets.QWidget(BrowseVideo)
        self.widget1.setGeometry(QtCore.QRect(40, 190, 481, 40))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(BrowseVideo)
        QtCore.QMetaObject.connectSlotsByName(BrowseVideo)

    def retranslateUi(self, BrowseVideo):
        _translate = QtCore.QCoreApplication.translate
        BrowseVideo.setWindowTitle(_translate("BrowseVideo", "Video Frame"))
        self.label.setText(_translate("BrowseVideo", "Upload a Video"))
        self.label_2.setText(_translate("BrowseVideo", "Choose a frame"))
        self.pushButton.setText(_translate("BrowseVideo", "Browse"))
        self.pushButton_2.setText(_translate("BrowseVideo", "Submit"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_handler2)

    def pushButton_handler(self):
        self.open_dialog_box()
    def open_dialog_box(self):

        filename = QFileDialog.getOpenFileName(filter="Videos (*.mp4 *.avi *.mov)")
        global path
        path = filename[0]
        self.lineEdit.setText(path)
        src = path
        vid=cv2.VideoCapture(src)
        #print(self.lineEdit.text())


    def pushButton_handler2(self):
        strpath = '"' + self.lineEdit.text() + '"'
        video = cv2.VideoCapture(path)
        frame = int(self.lineEdit_2.text())
        video.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret,img = video.read()
        #cv2.imwrite('image.png', img)

        img_bw=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Original', img)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

        # Split image to chromatic channels
        b, g, r = cv2.split(img)

        img[:, :, 0] = 0  # set blue channel to zero
        img[:, :, 1] = 0  # set green channel to zero
        img[:, :, 2] = 0  # set red channel to zero
        img_red = cv2.merge((img[:, :, 0], img[:, :, 1], r))  # (0,0,r)
        img_green = cv2.merge((img[:, :, 0], g, img[:, :, 2]))  # (0,g,0)
        img_blue = cv2.merge((b, img[:, :, 1], img[:, :, 2]))  # (b,0,0)
        cv2.imshow('Red', img_red)
        cv2.imshow('Green', img_green)
        cv2.imshow('Blue', img_blue)

        # Save image in different formats
        cv2.imwrite('imageRed.jpg', img_red)
        cv2.imwrite('imageRed.png', img_red)
        cv2.imwrite('imageRed.tiff', img_red)

        cv2.imwrite('imageGreen.jpg', img_green)
        cv2.imwrite('imageGreen.png', img_green)
        cv2.imwrite('imageGreen.tiff', img_green)

        cv2.imwrite('imageBlue.jpg', img_blue)
        cv2.imwrite('imageBlue.png', img_blue)
        cv2.imwrite('imageBlue.tiff', img_blue)

        Y, Cr, Cb = cv2.split(img2)

        cv2.imshow('Luminance', Y)
        img_cb = cv2.merge((Cb, Cr, img[:, :, 0]))
        cv2.imshow('Chroma blue', img_cb)
        img_cr = cv2.merge((img[:, :, 0], Cb, Cr))
        cv2.imshow('Chroma red', img_cr)

        cv2.waitKey(0)  # pressing any key on the keyboard continues the code
        cv2.destroyAllWindows()

        cv2.imshow('Grayscale', img_bw)
        cv2.waitKey(0)  # pressing any key on the keyboard continues the code
        cv2.destroyAllWindows()

        plt.figure("Grayscale Histogram")
        plt.hist(img_bw.ravel(), 256, [0, 256], color="gray")
        plt.figure("Red Histogram")
        plt.hist(r.ravel(), 256, [0, 256], color="red")
        plt.figure("Green Histogram")
        plt.hist(g.ravel(), 256, [0, 256], color="green")
        plt.figure("Blue Histogram")
        plt.hist(b.ravel(), 256, [0, 256], color="blue")

        plt.show()




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_BrowseVideo()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
