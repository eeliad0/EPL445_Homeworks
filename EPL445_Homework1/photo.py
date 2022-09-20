# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowsePhoto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2


from matplotlib import pyplot as plt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 206)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image-outline-filled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 120, 112, 38))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(16, 124, 367, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 204, 37))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Browse Photo"))
        self.label.setText(_translate("Form", "Image Browse"))
        self.pushButton.setText(_translate("Form", "Browse"))
        self.pushButton.clicked.connect(self.pushButton_handler)

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):

        filename = QFileDialog.getOpenFileName(filter="Images (*.png *.tiff .jpg)")
        path = filename[0]
        self.lineEdit.setText(path)
        src = path
        img = cv2.imread(src)
        img = cv2.resize(img, (600, 400), interpolation=cv2.INTER_AREA)
        img_bw = cv2.imread(src, 0)
        img_bw = cv2.resize(img_bw, (600, 400), interpolation=cv2.INTER_AREA)
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
        img_cb = cv2.merge((Cb, Cr, img[:, :, 0])) #(cb, cr, 0) midenizete to kokkino ara iparzoun mono prasines kai mple apoxrosis
        cv2.imshow('Chroma blue', img_cb)
        img_cr = cv2.merge((img[:, :, 0], Cb, Cr)) #(0, cb, cr) midenizete to mple ara iparxoun mono prasines kai kokkines apoxrosis
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
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


