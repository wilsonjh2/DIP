import sys
import os
from skimage import io

def evaluate(img):
	os.system("python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image="+str(img))#need error checking

args = sys.argv[1:] #get everything after main.py
os.system("IMAGE_SIZE=224") 
os.system('ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"')
		
#print(args)
for arg in args:
	if(arg == "-h"):
		print("Help")

	elif(arg == "-r"):
		print("Retrain")
		retrain()
		print('\n')
		
		os.system("IMAGE_SIZE=224") 
		os.system('ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"')

	elif(arg == "-e"):
		img = args[args.index(arg)+1] #need error checking here for when no img is given
		print("Evaluate")
		print("Probably got the image")
		evaluate(img)
	
	elif(arg == "-s"):
		print("Sort")
		#if sort, evalute each image in a directory and put them into sorted directorys
	
	else:
		print("")




 
