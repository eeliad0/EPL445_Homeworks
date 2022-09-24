
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import pi


class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 217)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("search-flat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Ligh")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Morphology Processing"))
        self.pushButton.setText(_translate("Form", "Browse image"))
        self.label.setText(_translate("Form", "Please select a morphology operator"))
        self.label_2.setText(_translate("Form", "Please select a structuring element"))
        self.comboBox.setItemText(0, _translate("Form", "Erosion"))
        self.comboBox.setItemText(1, _translate("Form", "Dilation"))
        self.comboBox.setItemText(2, _translate("Form", "Opening"))
        self.comboBox.setItemText(3, _translate("Form", "Closing"))
        self.comboBox_2.setItemText(0, _translate("Form", "Square (5x5)"))
        self.comboBox_2.setItemText(1, _translate("Form", "Square (9x9)"))
        self.comboBox_2.setItemText(2, _translate("Form", "Cross (5x5)"))
        self.comboBox_2.setItemText(3, _translate("Form", "Cross (9x9)"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton_3.setText(_translate("Form", "Save image"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_handler_2)
        self.pushButton_3.clicked.connect(self.pushButton_handler_3)

    def operation(self, op, kernel, img_orig):
        global str1, img
        str1 = op
        if (op == "Dilation"):
            img = cv2.dilate(img_orig, kernel, iterations=1)

        elif (op == "Erosion"):
            img = cv2.erode(img_orig, kernel, iterations=1)

        elif (op == "Opening"):
            img = cv2.morphologyEx(img_orig, cv2.MORPH_OPEN, kernel, iterations=1)

        elif (op == "Closing"):
            img = cv2.morphologyEx(img_orig, cv2.MORPH_CLOSE, kernel, iterations=1)

        else:
            print("error")

    def kernelProduce(self, shape):
        if (shape == "Cross (5x5)"):
            kernel = np.array([[0, 0, 1, 0, 0],
                               [0, 0, 1, 0, 0],
                               [1, 1, 1, 1, 1],
                               [0, 0, 1, 0, 0],
                               [0, 0, 1, 0, 0]], dtype=np.uint8)

        elif (shape == "Cross (9x9)"):
            kernel = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0]], dtype=np.uint8)
        elif (shape == "Square (5x5)"):
            kernel = np.ones((5, 5), np.uint8)
        elif (shape == "Square (9x9)"):
            kernel = np.ones((9, 9), np.uint8)
        else:
            print("error")
        return kernel

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(filter="Images (*.png *.tiff *.jpg)")
        global path
        path = filename[0]
        self.lineEdit.setText(path)

    def pushButton_handler_2(self):
        self.open_dialog_box_2()

    def open_dialog_box_2(self):
        imgOrig = cv2.imread(path)
        imgGray = cv2.imread(path, 0)
        if "dermatological" in path:
            imgOrig = cv2.resize(imgOrig, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
            imgGray = cv2.resize(imgGray, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
        ret, imgBinary = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Original", imgOrig)
        cv2.imshow("Grayscale", imgGray)
        cv2.imshow("Binary", imgBinary)
        ker = self.kernelProduce(self.comboBox_2.currentText())
        self.operation(self.comboBox.currentText(), ker, imgBinary)

        images = [imgOrig,
                  imgGray,
                  imgBinary,
                  img]
        titles = ['Original  Image',
                  'Grayscale Image',
                  'Binary Image',
                  str1]

        for i in range(4):
            plt.subplot(2, 2, i + 1),
            if(titles[i]=='Original  Image'):
                plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
            else:
                plt.imshow(images[i],'gray')
            plt.title(titles[i]),
            plt.xticks([]), plt.yticks([])
            plt.colorbar()
        plt.show()

    def pushButton_handler_3(self):
        self.open_dialog_box_3()

    def open_dialog_box_3(self):
        name,blank = QFileDialog.getSaveFileName(self, 'Save File','C:\\', filter="Images (*.jpg)")
        if(name):
            cv2.imwrite(name, img)
        else:
            print("error")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()