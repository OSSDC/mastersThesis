#!/usr/bin/python3

from PIL import Image
import os
import array
import time
import sys
import argparse
from ctypes import *
import numpy

numpy.set_printoptions(threshold=numpy.nan)
numpy.set_printoptions(linewidth=2000)

colorScheme = numpy.array([(0x00, 0x00, 0x8F), \
                           (0x00, 0x0F, 0xFF), \
                           (0x00, 0x8F, 0xFF), \
                           (0x00, 0xCF, 0xFF), \
                           (0x0F, 0xFF, 0xEF), \
                           (0x4F, 0xFF, 0xAF), \
                           (0x8F, 0xFF, 0x6F), \
                           (0xCF, 0xFF, 0x2F), \
                           (0xFF, 0xEF, 0x00), \
                           (0xFF, 0xAF, 0x00), \
                           (0xFF, 0x9F, 0x00), \
                           (0xFF, 0x6F, 0x00), \
                           (0xFF, 0x2F, 0x00), \
                           (0xEF, 0x00, 0x00), \
                           (0xAF, 0x00, 0x00), \
                           (0x7F, 0x00, 0x00)])

#fDisp = open('cDisp.txt', 'r')

disp = numpy.loadtxt('cDisp.txt', dtype='int')
[dispH, dispW] = disp.shape

'''for i in range(375):
    for j in range(361):
        if (disp[i][j] > 15):
            disp[i][j] = 15'''

# create disparity image
im = Image.new("RGB", (dispW, dispH), "black")

for i in range(dispW):
    for j in range(dispH):
        im.putpixel((i,j), (colorScheme[disp[j][i]][0], colorScheme[disp[j][i]][1], colorScheme[disp[j][i]][2]))

im.save("venus_c_7x7.png")
im.show()

#fDisp.close()

