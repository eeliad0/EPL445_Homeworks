# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import os
import numpy as np
import cv2
from glob import glob
from matplotlib import pyplot as plt
import skimage


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

    def pushButton_handler2(self):
        video = cv2.VideoCapture(path)
        frame = int(self.lineEdit_2.text())
        video.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret,img = video.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        noiseGaus = skimage.util.random_noise(img, mode="gaussian")
        noiseSpeckle =  noise = skimage.util.random_noise(img, mode="speckle")
        noiseSP = noise = skimage.util.random_noise(img, mode="s&p", amount=0.2)

        # Show Results
        plt.subplot(431), plt.imshow(noiseGaus, cmap="gray")
        plt.title('Gaussian Noise'), plt.xticks([]), plt.yticks([])
        plt.subplot(432), plt.imshow(noiseSP, cmap="gray")
        plt.title('S&P Noise'), plt.xticks([]), plt.yticks([])
        plt.subplot(433), plt.imshow(noiseSpeckle, cmap="gray")
        plt.title('Speckle Noise'), plt.xticks([]), plt.yticks([])
        plt.subplot(434), plt.imshow(cv2.blur(noiseGaus, (5, 5)), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(435), plt.imshow(cv2.blur(noiseSP, (5, 5)), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(436), plt.imshow(cv2.blur(noiseSpeckle, (5, 5)), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(437), plt.imshow(cv2.GaussianBlur(noiseGaus, (5, 5), 0), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(438), plt.imshow(cv2.GaussianBlur(noiseSP, (5, 5), 0), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(439), plt.imshow(cv2.GaussianBlur(noiseSpeckle, (5, 5), 0), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        noiseGaus = np.float32(noiseGaus)
        noiseSP = np.float32(noiseSP)
        noiseSpeckle = np.float32(noiseSpeckle)
        plt.subplot(4, 3, 10), plt.imshow( cv2.medianBlur(noiseGaus, 5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(4, 3, 11), plt.imshow( cv2.medianBlur(noiseSP, 5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(4, 3, 12), plt.imshow( cv2.medianBlur(noiseSpeckle, 5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])

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
