import numpy as np
import os
from skimage import io
import time
from PIL import Image

def diff(img, avg, name):
    img = np.round(np.dot(img[...,:3],[.3, .6, .1])).astype(int) 
    io.imsave('/home/jwilz222/Desktop/tensorflow-for-poets-2/grayscale/gray-'+name,img) 
    print("Avg size: " + str(avg.shape))
    print("Img size: " + str(img.shape))    
    g = np.ceil(avg-img).astype(int)
    io.imsave('/home/jwilz222/Desktop/tensorflow-for-poets-2/subimage/diff-'+name, g) 

def crop(f, x):
    #f = np.delete(f, np.s_[0:850], 0)
    #f = np.delete(f, np.s_[299:], 0)
    #f = np.delete(f, np.s_[0:1230], 1)
    #f = np.delete(f, np.s_[299:], 1)
    
    io.imsave('/home/jwilz222/Desktop/tensorflow-for-poets-2/outputs/output-'+x, f) 
    #returning 
    return f 

start = time.time()     
#sumI = np.int64(np.zeros((299,299, 3))) 
sumI = np.int64(np.zeros((1920,2560, 3))) 
count = 0

for file in os.listdir('101MEDIA'):
   print("Count: " + str(count))
   x = str(file)
   f = io.imread('/home/jwilz222/Desktop/tensorflow-for-poets-2/101MEDIA/' + x)
   croppedImage = crop(f, x)     
   sumI = sumI + croppedImage
   count = count + 1
   continue

avgMatrix = (np.round(np.divide(sumI, count))).astype(int)

gImage = np.round(np.dot(avgMatrix[...,:3],[.3, .6, .1])).astype(int) 
io.imsave("Average.png", gImage)

#
for file in os.listdir('outputs'):
   y = str(file)
   g = io.imread('/home/jwilz222/Desktop/tensorflow-for-poets-2/outputs/' +y)
   diff(g, gImage, y)
   continue

end = time.time()
print("Runtime: " + str(end-start))
