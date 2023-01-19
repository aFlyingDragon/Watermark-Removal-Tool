import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import cv2
from skimage.color import rgb2lab, deltaE_cie76
from collections import Counter
from tkinter import filedialog as fd
import tkinter
import os

#Will currently read the data from a single image
#Will only read the first image in a multi-image file
#Add support if necessary
#RGB code to be changed are: 149,149,149 | 214,214,214 | 178,178,178
def main():
    filename = fd.askopenfilename()
    print(filename)
    pic=imageio.imread(filename)
    start=0
    x=pic.shape[0]
    y=pic.shape[1]
    ask = tkinter.simpledialog.askinteger('RGB Value', 'Please input the integer value of the pixel you wish to remove (0-255):', minvalue=0,maxvalue=255)
##Need to make this window show up when the other window shows up
    for pixel_x in range(start,x):
        for pixel_y in range(start,y):
            for RGB in range(0,3):
                pixel_to_edit = (pic[pixel_x,pixel_y,RGB])
####                medium_gray=(pic[pixel_x,pixel_y,RGB] == 178)
####                lightest_gray = (pic[pixel_x,pixel_y,RGB] == 214)
##                pixel_left = (pic[pixel_x-1,pixel_y,RGB] == 254)
##                pixel_right = (pic[pixel_x+1,pixel_y,RGB] == 254)
##                pixel_up = (pic[pixel_x,pixel_y+1,RGB] == 254)
##                pixel_down = (pic[pixel_x,pixel_y-1,RGB]==254)
                if (pixel_to_edit) in range(ask, 254):# and (pixel_left and pixel_right):
                   pixel_to_edit = 254
    plt.figure(figsize=(10,10))
    plt.imshow(pic)
    plt.show()
    filename.save(plt.imshow(pic))
    

main()
