from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import pi
import math

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 329)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 160, 441, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.regionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.regionLineEdit.setObjectName("regionLineEdit")
        self.verticalLayout_5.addWidget(self.regionLineEdit)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 240, 441, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.submitButton = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(9)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout_6.addWidget(self.submitButton)
        self.saveButton = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(9)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_6.addWidget(self.saveButton)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 441, 63))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pathLineEdit = QtWidgets.QLineEdit(self.widget2)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.browseButton = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(9)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout.addWidget(self.browseButton)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(280, 90, 171, 47))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.radius2LineEdit = QtWidgets.QLineEdit(self.widget3)
        self.radius2LineEdit.setObjectName("radius2LineEdit")
        self.verticalLayout_4.addWidget(self.radius2LineEdit)
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(130, 90, 141, 47))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.radiusLineEdit = QtWidgets.QLineEdit(self.widget4)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.verticalLayout_3.addWidget(self.radiusLineEdit)
        self.widget5 = QtWidgets.QWidget(Form)
        self.widget5.setGeometry(QtCore.QRect(10, 90, 111, 47))
        self.widget5.setObjectName("widget5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.PassComboBox = QtWidgets.QComboBox(self.widget5)
        self.PassComboBox.setObjectName("PassComboBox")
        self.PassComboBox.addItem("")
        self.PassComboBox.addItem("")
        self.PassComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.PassComboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Homework 3"))
        self.label_5.setText(_translate("Form", "Select Image Region"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.saveButton.setText(_translate("Form", "Save Image"))
        self.label.setText(_translate("Form", "Image Path"))
        self.browseButton.setText(_translate("Form", "Browse Image"))
        self.label_4.setText(_translate("Form", "Give 2nd Radius (optional)"))
        self.label_3.setText(_translate("Form", "Give Radius"))
        self.label_2.setText(_translate("Form", "Select Mask"))
        self.PassComboBox.setItemText(0, _translate("Form", "Low Pass"))
        self.PassComboBox.setItemText(1, _translate("Form", "Mid Pass"))
        self.PassComboBox.setItemText(2, _translate("Form", "High Pass"))
        self.browseButton.clicked.connect(self.browseButton_handler)
        self.submitButton.clicked.connect(self.submitButton_handler)



    def browseButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        global path,img
        if self.pathLineEdit.text()=="cos_img":
            N = 64
            Icos = mask = np.zeros((N, N))
            for i in range(0, N):
                for j in range(0, N):
                    Icos[i, j] = 0.5 * math.cos(((2 * math.pi) / N) * ((8 * i) + (6 * j))) + 1.5 * math.cos(
                        ((2 * math.pi) / N) * ((4 * i) + (2 * j))) + math.cos(((2 * math.pi) / N) * ((2 * j)))
            plt.imshow(Icos, cmap='gray')
            img=Icos
            plt.title('COS Image'), plt.xticks([]),
            plt.yticks([])
            plt.show()
        else:
           filename = QFileDialog.getOpenFileName(filter="Images (*.png *.tiff *.jpg)")
           path = filename[0]
           self.pathLineEdit.setText(path)
           imgOrig = cv2.imread(path)
           img = imgGray = cv2.imread(path, 0)
           if "dermatological" in path:
               imgOrig = cv2.resize(imgOrig, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
               imgGray = cv2.resize(imgGray, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
           #ret, imgBinary = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
           cv2.imshow("Original", imgOrig)
           cv2.imshow("Grayscale", imgGray)
           #cv2.imshow("Binary", imgBinary)

    def submitButton_handler(self):
        self.open_dialog_box2()

    def open_dialog_box2(self):
        self.fourier_fun()
    def fourier_fun(img,mask,r):
        rows, cols = img.shape

        # Find the center (values are float)
        crow, ccol = rows / 2, cols / 2
        # Convert values to integer to be used as index
        crow = np.int(crow)
        ccol = np.int(ccol)

        f = np.fft.fft2(img)
        # Shift the zero-frequency component (DC component) to the center of the spectrum
        fshift = np.fft.fftshift(f)
        # Magnitude spectrum using log transformation
        magnitude_spectrum = np.log(1 + np.abs(fshift))
        boundary = 50
        if mask=="High Pass" :
            mask = np.ones(img.shape, np.uint8)
            mask[crow - boundary:crow + boundary, ccol - boundary:ccol + boundary] = 0

            # Apply high pass
            fshift = fshift * mask

            # Apply inverse FFT
            f_back = np.fft.ifftshift(fshift)
            img_back = np.fft.ifft2(f_back)
            img_back = np.real(img_back)
        elif mask=="Low Pass":
            # Create low pass
            mask = np.zeros(img.shape, np.uint8)
            mask[crow - boundary:crow + boundary, ccol - boundary:ccol + boundary] = 1

            # Apply low pass
            fshift = fshift * mask

            # Apply inverse FFT
            f_back = np.fft.ifftshift(fshift)
            img_back = np.fft.ifft2(f_back)
            img_back = np.real(img_back)
        elif mask=="Mid Pass" :
            # Set mask boundaries
            boundary1 = 80
            boundary2 = 100

            # Create mid pass
            mask = np.zeros((rows, cols), np.uint8)
            mask[crow - boundary2:crow + boundary2, ccol - boundary2:ccol + boundary2] = 1
            mask[crow - boundary1:crow + boundary1, ccol - boundary1:ccol + boundary1] = 0

            # Apply mid-pass
            fshift = fshift * mask

            # Apply inverse FFT
            f_back = np.fft.ifftshift(fshift)
            img_back = np.fft.ifft2(f_back)
            img_back = np.real(img_back)
        else:
             print("Error")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

