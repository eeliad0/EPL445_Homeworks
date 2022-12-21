# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2frame.ui'
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
vid=""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 276)
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(50, 10, 381, 231))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Browse Video"))
        self.pushButton.setText(_translate("Form", "Browse"))
        self.label_2.setText(_translate("Form", "Frame 1"))
        self.label_3.setText(_translate("Form", "Frame 2"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_handler2)

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(filter="Videos (*.mp4 *.avi *.mov)")
        global path
        path = filename[0]
        self.lineEdit.setText(path)
        # print(self.lineEdit.text())

    def pushButton_handler2(self):
        strpath = '"' + self.lineEdit.text() + '"'
        video = cv2.VideoCapture(path)
        print("here")
        video2 = cv2.VideoCapture(path)
        frame = int(self.lineEdit_2.text())
        frame2 = int(self.lineEdit_3.text())
        video.set(cv2.CAP_PROP_POS_FRAMES, frame)
        video2.set(cv2.CAP_PROP_POS_FRAMES, frame2)
        ret,img = video.read()
        ret,img2 = video2.read()
        img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2_bw = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(img, img2)
        diff_bw = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        #Show Results
        plt.subplot(431), plt.imshow(img_bw, cmap="gray")
        plt.title('Frame 1'), plt.xticks([]), plt.yticks([])
        plt.subplot(432), plt.imshow(img2_bw, cmap="gray")
        plt.title('Frame 2'), plt.xticks([]), plt.yticks([])
        plt.subplot(433), plt.imshow(diff_bw, cmap="gray")
        plt.title('Abs Diff'), plt.xticks([]), plt.yticks([])
        plt.subplot(434), plt.imshow(self.CannyAlg(img_bw), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(435), plt.imshow(self.CannyAlg(img2_bw), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(436), plt.imshow(self.CannyAlg(diff_bw), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(437), plt.imshow(cv2.Laplacian(img_bw, cv2.CV_64F), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(438), plt.imshow(cv2.Laplacian(img2_bw, cv2.CV_64F), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(439), plt.imshow(cv2.Laplacian(diff_bw, cv2.CV_64F), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(4,3,10), plt.imshow(cv2.Sobel(img_bw, cv2.CV_64F, 0, 1, ksize=5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(4,3,11), plt.imshow(cv2.Sobel(img2_bw, cv2.CV_64F, 0, 1, ksize=5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])
        plt.subplot(4,3,12), plt.imshow(cv2.Sobel(diff_bw, cv2.CV_64F, 0, 1, ksize=5), cmap="gray")
        plt.title(''), plt.xticks([]), plt.yticks([])

        plt.show()


    def CannyAlg(self,image):
        sigma = 0.33  # threshold
        v = np.median(image)  # find median
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))  # find lower bound
        upper = int(min(255, (1.0 + sigma) * v))  # find upper bound
        edges = cv2.Canny(image, lower, upper)
        return edges


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
