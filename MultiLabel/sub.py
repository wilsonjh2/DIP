import numpy as np
import os
from skimage import io
import time
from PIL import Image

inputImg = "int.jpg"
img = io.imread(str(inputImg))
avg = io.imread("average.png")

img = np.round(np.dot(img[...,:3],[.3,.6,.1])).astype(int)
maxI = 0
g = np.ceil(avg-img).astype(int)
for i in range(g.shape[0]):
	for j in range(g.shape[1]):
		if(g[i,j] < 50):
			g[i,j] =  0
		else:
			g[i,j] = 255
	#if(g[i, j] < 200):
		#	g[i,j] = 0
io.imsave('output5.jpg', g)
print("MAX: " + str(maxI))
