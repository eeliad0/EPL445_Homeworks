# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from Huffman3 import huffman, encode, decode, makenodes, iterate
import collections
import cv2
from matplotlib import pyplot as plt
import numpy as np
import sys
from Huffman3 import encode, decode, makenodes, iterate
from zigzag import zigzag, inverse_zigzag

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
        self.pushButtonSubmit.clicked.connect(self.submitButtonHandler)

    def pushButton_handler(self):
        self.browseImage()

    def browseImage(self):
        filename = QFileDialog.getOpenFileName(filter="Images (*.jpg *.png *.tif)")
        global path
        path = filename[0]
        self.lineEdit.setText(path)
        global img

        img = cv2.imread(path,0)
        img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
        global q_table
        q_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                           [12, 12, 14, 19, 26, 58, 60, 55],
                           [14, 13, 16, 24, 40, 57, 69, 56],
                           [14, 17, 22, 29, 51, 87, 80, 62],
                           [18, 22, 37, 56, 68, 109, 103, 77],
                           [24, 35, 55, 64, 81, 104, 113, 92],
                           [49, 64, 78, 87, 103, 121, 120, 101],
                           [72, 92, 95, 98, 112, 100, 103, 99]], dtype=np.float32)

    def submitButtonHandler(self):
        self.imgCompression(self.lineEditMF.text())
    def dctComp(self,block):
        block_f = np.float32(block)
        block_dct.append(cv2.dct(block_f))

    def quantComp(self,block):
        block_q.append(np.floor(np.divide(block_dct, q_table_factor) + 0.5))

    def zigzagComp(self,block):
        vector_zigzag.append(zigzag(block))

    def dpcmComp(self,count):
            for k in range(1, 8):
                e[count].append(vector_zigzag[(k * 8)] - vector_zigzag[(k - 1) * 8])

    def imgCompression(self, factor):

        factor = float(factor)
        # step one: 8x8 blocks &apply DCT to each block
        vector_blocks = [[]]
        iHeight, iWidth = img.shape
        counter=0
        global block_dct
        block_dct = []
        global block_q
        block_q=[]
        global vector_zigzag
        vector_zigzag=[[]]
        # Image partitioned into 8x8 blocks
        for startY in range(0, img.shape[0]-8, 8):
            for startX in range(0, img.shape[1]-8, 8):
                block = img[startY:startY + 8, startX:startX + 8]
                print(block,counter)
                vector_blocks.append(block)
                self.dctComp(vector_blocks[counter])
                counter = counter + 1
        global q_table_factor
        q_table_factor = np.multiply(q_table, factor)
        counter = 0
        for startY in range(0, img.shape[0]-8, 8):
            for startX in range(0, img.shape[1]-8, 8):
                self.quantComp(block_dct[counter])
                counter=counter+1
        counter=0
        for startY in range(0, img.shape[0]-8, 8):
            for startX in range(0, img.shape[1]-8, 8):
                self.zigzagComp(block_q[counter])
                counter=counter+1

        global e
        e=[[]]
        e[0].append(vector_zigzag[0])
        counter=0
        for startY in range(0, img.shape[0]-8, 8):
            for startX in range(0, img.shape[1]-8, 8):
                self.dpcmComp(counter)

        # step five: RLC for AC values
        zero_count = 0
        pos = 0
        ac = []
        for i in range(64):
            if(vectors_zigzag[i]==0):
                zero_count = zero_count+1
            else:
                ac.append([zero_count,vectors_zigzag[i]])
                zero_count = 0

            if(i==63):
                ac.append([0,0])
        # step six: Huffman encoding
        # for DC difference values
        # Find frequency of appearance for each value of the list
        counter1 = collections.Counter(e)
        # Define list of probabilities as list of pairs (Unique item, Corresponding frequency)
        probs1 = []
        # Initialization of probabilities' list
        for key, value in counter1.items():
            probs1.append((key, np.float32(value)))
        # Creates a list of nodes ready for the Huffman algorithm 'iterate'.
        symbols1 = makenodes(probs1)
        # Runs the Huffman algorithm on a list of "nodes". It returns a pointer to the root of a new tree of "internal nodes".
        root1 = iterate(symbols1)
        s1 = encode(e, symbols1)

        # Inverse to get the Compressed Image
        # Huffman Decoding
        list_decode_dpcm = decode(s1, root1)
        #Inverse DPCM
        ie = []
        ie.append(list_decode_dpcm[0])
        for k in range(1, len(list_decode_dpcm)):
            ie.append(list_decode_dpcm[k] + ie[k - 1])
        # Inverse ZigZag
        inverseZigZag = inverse_zigzag(vectors_zigzag, 8, 8)
        # Inverse Quantization
        q_table_factor = np.multiply(q_table,factor)
        blockT = np.multiply(inverseZigZag, q_table_factor)
        # Inverse DCT
        block_idct = cv2.idct(blockT)
        Iblock = np.float32(block_idct)






def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
