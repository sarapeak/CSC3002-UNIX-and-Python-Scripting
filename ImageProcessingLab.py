# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:04:12 2021

@author: sarap
"""
from PIL import Image
from numpy import *

picture = input ('What picture file would you like to add a border to? ')
result = input ('Where would you like to store the result? ')
red = input ('How much red in the frame? ')
green = input ('How much green in the frame? ')
blue = input ('How much blue in the frame? ')

imagePic = Image.open(picture)
picArray = array(imagePic)

arrayShape = picArray.shape
rows = arrayShape[0]
columns = arrayShape[1]

for i in range (10):
    for j in range (10):
        picArray[i,j,0] = red
        picArray[i,j,1] = green
        picArray[i,j,2] = blue
        
newImage = Image.fromarray(picArray)
newImage.save(result)

print ('Done!')