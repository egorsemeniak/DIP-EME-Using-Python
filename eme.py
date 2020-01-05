#importing required libaries
import numpy as np
import cv2
import math
#creating an image file using imread
img = cv2.imread('5.jpg',0)#replace the file name with a file/folder on your machine
def getEME(img):
	rows, cols = img.shape
	tempv1 = int(round(cols/100))
	tempv2 = int(round(rows/100))
	eme = 0
	#calculations for EME
	for r in range(0, img.shape[0] - tempv1, tempv1):
		for c in range(0, img.shape[1] - tempv2, tempv2):
			imgTemp = img[r:r+10, c:c+10]
			if((imgTemp.min() == 0)or(imgTemp.max() ==0)):
					temp2 = imgTemp.min()+0.00001
					temp3 = imgTemp.max()+0.00001
					eme += 20*math.log(temp3/temp2)
			else:
					eme += 20*math.log(imgTemp.max()/imgTemp.min())
	eme = eme/10000
	print ("EME =", eme)

getEME(img)
