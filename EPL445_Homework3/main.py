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
N = 64
Icos = mask = np.zeros((N, N))
for i in range(0, N):
  for j in range(0, N):
     Icos[i, j] = 0.5*math.cos(((2*math.pi)/N)*((8*i)+(6*j))) +1.5*math.cos(((2*math.pi)/N)*((4*i)+(2*j))) + math.cos(((2*math.pi)/N)*((2*j)))
#f = np.fft.fft2(Icos)
#fshift = np.fft.fftshift(f)
plt.imshow(Icos, cmap = 'gray')

plt.title('COS Image'), plt.xticks([]),
plt.yticks([])
plt.show()