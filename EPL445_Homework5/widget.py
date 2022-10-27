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
from skimage.metrics import structural_similarity as ssim
from zigzag import zigzag, inverse_zigzag
import math
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 343)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
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
        Form.setWindowTitle(_translate("Form", "Image Compression"))
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

    def imgCompression(self, factor):
        dpcm = []
        jpeg = []
        prevDc = 0
        iHeight, iWidth = img.shape[:2]
        factor = float(factor)
        q_table_factor = np.multiply(q_table, factor)
        for startY in range(0, iHeight, 8):
            for startX in range(0, iWidth, 8):
                block = img[startY:startY + 8, startX:startX + 8]
                # apply DCT for a block
                block_f = np.float32(block)
                dst = cv2.dct(block_f)
                # Quantization in each block
                block_q = np.floor(np.divide(dst, q_table_factor) + 0.5)
                # Make zigzag table
                zigzag_table = (zigzag(block_q))
                dpcm.append((zigzag_table[0] - prevDc))
                prevDc = zigzag_table[0]
                #RLC
                zigzag_table.pop(0)
                rlc = []
                count = 0
                # Apply the RLC for all the elements from the zig zag table
                for i in zigzag_table:
                    if i == 0:
                        count += 1
                        continue
                    else:
                        rlc.append(count)
                        rlc.append(i)
                        count = 0
                rlc.append(0)
                rlc.append(0)
                # create huffman algorithm for this block
                jpeg.append(huffman(rlc))
        # the compressed image
        jpeg.append(huffman(dpcm))

        # decompress the image
        dec = []
        # all except last row are the DC
        for i in jpeg[:-1]:
            current = [float(j) for j in decode(i[0], i[1])]
            array = []
            if len(current) == 0:
                for l in range(63):
                    array.append(0)
            for k in range(0, len(current), 2):
                # if this is the last element
                if int(current[k]) == 0 and int(current[k + 1]) == 0:
                    # apply the rest with 0 until 64 is completed.
                    for l in range(63 - len(array)):
                        array.append(0.0)
                    break
                if int(current[k]) != 0:
                    # append the number of zeros we had before the number
                    for l in range(int(current[k])):
                        array.append(0.0)
                # append the number after the zeros
                array.append(current[k + 1])
            dec.append(array)
        c = 0
        # decode the DC table
        dc = decode(jpeg[-1][0], jpeg[-1][1])
        for i in dc:
            if c == 0:
                dec[0].insert(0, float(i))
            else:
                dec[c].insert(0, float(i) + float(dec[c - 1][0][0]))
            dec[c] = np.array(dec[c])
            # inverse zig zag
            dec[c] = inverse_zigzag(dec[c].astype(int))
            c += 1
        # our decompressed image table
        img_comp = np.empty(shape=(iHeight, iWidth))
        temp = []
        for i in dec:
            # inverse the quantization for each block
            iblock_q = np.floor(np.multiply(i, q_table_factor) + 0.5)
            # inverse the dct
            inv_dct = cv2.idct(iblock_q)
            np.place(inv_dct, inv_dct > 255.0, 255.0)
            np.place(inv_dct, inv_dct < 0.0, 0.0)
            temp.append(inv_dct)
        k = 0
        # reorganise the block to create the image in its original structure.
        for startY in range(0, iHeight, 8):
            for startX in range(0, iWidth, 8):
                img_comp[startY:startY + 8, startX:startX + 8] = temp[k]
                k += 1

        if(path[-3:]=="tif"):
            cv2.imwrite('original.tif', img)
            cv2.imwrite('compressed.tif', img_comp)
        elif(path[-3:]=="png"):
            cv2.imwrite('original.png', img)
            cv2.imwrite('compressed.png', img_comp)
        else:
            print("wrong image format")


        mse = np.mean((img - img_comp) ** 2)
        pnsr = 10 * np.log10(math.pow(255, 2) / mse)
        ssim_value = ssim(img, img_comp, data_range=img.max() - img.min())

        img_size = os.path.getsize('original.tif')
        comp_size = os.path.getsize('compressed.tif')
        cr = img_size / comp_size

        print("mse ", mse)
        print("pnsr ", pnsr)
        print("ssim ", ssim_value)
        print("compression rate", cr)

        self.lineEditMSE.setText(str(mse))
        self.lineEditPNSR.setText(str(pnsr))
        self.lineEditSSIM.setText(str(ssim_value))
        self.lineEditComp.setText(str(cr))

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Initial Picture'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_comp, cmap='gray')
        plt.title("Image after jpg algorithm"), plt.xticks([]), plt.yticks([])
        plt.show()

def huffman( list):
    counter = collections.Counter(list)
    size = 16 * len(set(list))
    probs = []
    # Initialization of probs list
    for key, value in counter.items():
        probs.append((key, np.float32(value)))
    symbols = makenodes(probs)
    root = iterate(symbols)
    s = encode(list, symbols)
    return (s, root, size)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
