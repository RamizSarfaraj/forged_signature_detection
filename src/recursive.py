import glob
import os
import sys
import matplotlib.pyplot as plt
import cv2


directory = "/home/ramiz/signatureDetection/Signs/Processed-Original/English"

imagelist = []

for filename in glob.iglob(directory + "**/**/*.jpg", recursive=True):
	imagelist.append(filename)


# print(len(imagelist))
# print(imagelist[2222])

data = []
for word in imagelist:
	if word == 'Eng':
		data.append(1)
	else:
		data.append(0)

print(len(data))
print(data[1222])



