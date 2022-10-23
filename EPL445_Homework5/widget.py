# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 343)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(25, 13, 239, 21))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonSubmit = QtWidgets.QPushButton(Form)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(130, 280, 201, 28))
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(23, 100, 411, 170))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEditMF = QtWidgets.QLineEdit(self.widget)
        self.lineEditMF.setObjectName("lineEditMF")
        self.verticalLayout_2.addWidget(self.lineEditMF)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.lineEditMSE = QtWidgets.QLineEdit(self.widget)
        self.lineEditMSE.setObjectName("lineEditMSE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditMSE)
        self.lineEditPNSR = QtWidgets.QLineEdit(self.widget)
        self.lineEditPNSR.setObjectName("lineEditPNSR")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPNSR)
        self.lineEditSSIM = QtWidgets.QLineEdit(self.widget)
        self.lineEditSSIM.setObjectName("lineEditSSIM")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditSSIM)
        self.lineEditComp = QtWidgets.QLineEdit(self.widget)
        self.lineEditComp.setObjectName("lineEditComp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditComp)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(25, 40, 411, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Browse and Show Image Path"))
        self.pushButtonSubmit.setText(_translate("Form", "Submit"))
        self.label_2.setText(_translate("Form", "Give Multiplying Factor"))
        self.label_3.setText(_translate("Form", "MSE"))
        self.label_4.setText(_translate("Form", "PNSR"))
        self.label_5.setText(_translate("Form", "SSIM"))
        self.label_6.setText(_translate("Form", "Compression"))
        self.pushButton.setText(_translate("Form", "Browse"))
        self.pushButton.clicked.connect(self.pushButton_handler)

    def pushButton_handler(self):
        self.browseImage()

    def browseImage(self):
        filename = QFileDialog.getOpenFileName(filter="Images (*.png *.tiff *.jpg)")
        global path
        path = filename[0]
        self.lineEdit.setText(path)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
