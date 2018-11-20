# program: Distortion.py
# author: Avnish K. Pandey
# Credits: Trevor M. Tomesh
# course: CS 827
# date: October 18th 2018
# description: this program reads mysteryTones.wav file,converts it mysteryTones_clipped.dat 
#	       file with space delimited PCM data, applies a user defined clipping filter and 
#	       writes out to a mysteryTones_clipped.wav file, converts it to mysteryTones_clipped.wav.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import subprocess 

#Converting .wav file to .dat file format
fileIn = subprocess.call(["sox", "mysteryTones.wav","mysteryTones.dat"]) 

#Absolute path to the file
data = pd.read_csv("D:/study/ComputerAudio/assignment3/mysteryTones.dat", skiprows=3,header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
xlist = []
ylist = []

# populate the lists with the contents of the columns read
for i in range(0,int(len(x))):
	xlist.append(float(x.iloc[i]))
	ylist.append(float(y.iloc[i]))

#Finding max amplitude value
max_value = max(ylist)

#Threshold value for clipping
threshold_value = float(input("Please enter the threshold value for clipping between 0.0 - "+str (max_value)+"? "))

f = open("mysteryTones_clipped.dat", "w")


# add header required for pcm file
f.write("; Sample Rate "+str(44100)+"\n")
f.write("; Channels 1"+"\n")

# hard-clipping filter
# It clips the values from the signal that are above or
# below threshold value and sets them to threshold value


newAmplitude = threshold_value
for i in range(0,int(len(xlist))):
	if ylist[i]>newAmplitude:
		ylist[i]=newAmplitude
		f.write(str(xlist[i])+"   "+str(((ylist[i])))+'\n')  
	elif ylist[i]<(-newAmplitude):
		ylist[i]=(-newAmplitude)
		f.write(str(xlist[i])+"   "+str(((ylist[i])))+'\n')
	else:
		f.write(str(xlist[i])+"   "+str(((ylist[i])))+'\n')


f.close()

#Converting .dat file to .wav file format
fileOut = subprocess.call(["sox", "mysteryTones_clipped.dat","mysteryTones_clipped.wav"])

