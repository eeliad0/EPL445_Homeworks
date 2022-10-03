from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import pi
import math

print("Hello World mlk")
print("ELLIEEEEEEEEEEEEEEEEEEEEEEEEEEE SOVAREFTOUUUUUUUUU")

#img=cv2.imread("logo2.png")
N = 64
Icos = mask = np.zeros((N, N))
for i in range(0, N):
  for j in range(0, N):
     Icos[i, j] = 0.5*math.cos(((2*math.pi)/N)*((8*i)+(6*j))) +1.5*math.cos(((2*math.pi)/N)*((4*i)+(2*j))) + math.cos(((2*math.pi)/N)*((2*j)))
#f = np.fft.fft2(Icos)
#fshift = np.fft.fftshift(f)
plt.imshow(Icos, cmap = 'gray')
img=Icos
plt.title('COS Image'), plt.xticks([]),
plt.yticks([])
plt.show()
#rows, cols = img.shape




f = np.fft.fft2(img)
# Shift the zero-frequency component (DC component) to the center of the spectrum
fshift = np.fft.fftshift(f)
# Magnitude spectrum using log transformation
magnitude_spectrum = np.log(1 + np.abs(fshift))


rows, cols = img.shape

# Find the center (values are float)
crow, ccol = rows/2 , cols/2
r1=15
r2=20
#crow = np.int(crow)
#ccol = np.int(ccol)

mask = np.zeros(img.shape, np.uint8)
for i in range (0,rows):
    for j in range(0, cols):
        point=math.sqrt(math.pow((i-crow),2)+math.pow((j-ccol),2))
        if point>=r1 :
            if point<r2:
             mask[i,j]=1
#        else:
#           mask[i,j]=0
#mask[-crow:crow , -ccol:ccol] <= radius



f_back = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_back)
img_back = np.real(img_back)
dft =np.fft.fft2(Icos, axes=(0,1))

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.axis("off")
plt.subplot(223),plt.imshow(magnitude_spectrum, cmap = 'gray'), plt.colorbar(cmap = 'gray',fraction=0.03, pad=0.04)
plt.title('Magnitude Spectrum'), plt.axis("off")
plt.subplot(222),plt.imshow(mask, cmap = 'gray')
plt.title('Mask'), plt.axis("off")
plt.subplot(224),plt.imshow(np.abs(img_back), cmap = 'gray')
plt.title('Inverse FFT image'), plt.axis("off")
plt.show()