from skimage import io
import numpy as np


f= io.imread('nobee.jpg')
shape = f.shape
print(shape)
flowerLeft = 0
half_X_Left = shape[0]/2
half_X_Right = half_X_Left
print("Half: " + str(half_X_Left))
#Trim the left and right sides
for j in range(shape[1]):
	pixel = f[half_X_Left,j]
	red = pixel[0]
	green = pixel[1]
	blue = pixel[2]

	if(red >180 and red < 230 and green > 140 and green < 179 and blue > 30 and blue < 59):
		#Reached the left side of the flower
		flowerLeft = [half_X_Left, j]		
		#print("Location: " + str(half_X_Left) + "," + str(j))
		#f[half_X_Left, j] = 0
print(flowerLeft)
g = np.array(f)
g = np.delete(g, np.s_[flowerLeft[1]:shape[1]], 1)


g = np.delete(g, np.s_[0:(g.shape[1]-1200)],1)
io.imsave('test.jpg',g)


 
