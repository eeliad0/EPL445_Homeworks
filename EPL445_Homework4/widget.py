
import skimage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import pi
import math
import os

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(579, 188)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 551, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLinEdit = QtWidgets.QLineEdit(self.widget)
        self.pathLinEdit.setObjectName("pathLinEdit")
        self.horizontalLayout.addWidget(self.pathLinEdit)
        self.browseButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Noise and Filter Selection"))
        self.label.setText(_translate("Form", "Image path"))
        self.browseButton.setText(_translate("Form", "Browse Image"))
        self.label_2.setText(_translate("Form", "Choose noise"))
        self.comboBox.setItemText(0, _translate("Form", "Gaussian"))
        self.comboBox.setItemText(1, _translate("Form", "Localvar"))
        self.comboBox.setItemText(2, _translate("Form", "Poisson"))
        self.comboBox.setItemText(3, _translate("Form", "Salt & Pepper"))
        self.comboBox.setItemText(4, _translate("Form", "Speckle"))
        self.label_3.setText(_translate("Form", "Choose filter"))
        self.comboBox_2.setItemText(0, _translate("Form", "Averaging"))
        self.comboBox_2.setItemText(1, _translate("Form", "Gaussian"))
        self.comboBox_2.setItemText(2, _translate("Form", "Median"))
        self.comboBox_2.setItemText(3, _translate("Form", "Laplacian"))
        self.comboBox_2.setItemText(4, _translate("Form", "Sobel"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.browseButton.clicked.connect(self.browseButton_handler)
        self.pushButton.clicked.connect(self.submitButton_handler)

    def browseButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        global path
        filename = QFileDialog.getOpenFileName(filter="Images (*.png *.tiff *.jpg)")
        path = filename[0]
        self.pathLinEdit.setText(path)


    def noise_select(self,img):
        global noise, titleNoise
        titleNoise=self.comboBox.currentText()

        if titleNoise == 'Gaussian':
            noise = skimage.util.random_noise(img, mode="gaussian")

        elif titleNoise == 'Localvar':
            noise = skimage.util.random_noise(img, mode="localvar")

        elif titleNoise == 'Poisson':
            noise = skimage.util.random_noise(img, mode="poisson")

        elif titleNoise == 'Salt & Pepper':
            noise = skimage.util.random_noise(img, mode="s&p", amount=0.2)

        elif titleNoise == 'Speckle':
            noise = skimage.util.random_noise(img, mode="speckle")

        else:
            print("error")

    def filter_select(self,img):
        global filter, titleFilter
        titleFilter=self.comboBox_2.currentText()

        if titleFilter=='Averaging':
            filter = cv2.blur(img, (5, 5))

        elif titleFilter=='Gaussian':
            filter = cv2.GaussianBlur(img, (5, 5), 0)

        elif titleFilter=='Median':
            img=np.float32(img)
            filter = cv2.medianBlur(img, 5)

        elif titleFilter=='Laplacian':
            filter = cv2.Laplacian(img, cv2.CV_64F)

        elif titleFilter=='Sobel':
            filter = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5) #sobelx

        else:
            print("error")


    def submitButton_handler(self):
        self.submitButton_dialogBox()

    def submitButton_dialogBox(self):
        imgOrig = cv2.imread(path,0)
        self.noise_select(imgOrig)
        self.filter_select(noise)
        plt.subplot(131), plt.imshow(imgOrig, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(noise, cmap='gray')
        plt.title(titleNoise+' Noise'), plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(filter, cmap='gray')
        plt.title(titleFilter+' Filter'), plt.xticks([]), plt.yticks([])

        plt.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

