#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:37:34 2019

@author: user
"""

import matplotlib.pyplot as plt				
import math				
import numpy as np				
from scipy.stats import linregress				
x=[20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340]				
y=[20,40,60,80,100,120,140,160,180]				
data2d = [43,23,25,32,46,55,55,72,73,92,73,56,37,54,33,26,16]				
data_add =[59,49,58,86,83,111,128,164,146]				
				
#error=list(np.array(data2d)**(1/2))				
#errorbars=np.round(np.array(error),2)				
#print(errorbars)				
#plt.bar(x,data2d,width=15,align="center",color="cyan",yerr=errorbars)				
#plt.show()				
				
#error=list(np.array(data_add)**(1/2))				
#errorbars=np.round(np.array(error),2)				
#print(errorbars)				
#plt.bar(y,data_add,width=15,align="center",color="cyan",yerr=errorbars)				
#plt.show()				
				
sinus=[0.17,0.34,0.5,0.64,0.76,0.86,0.94,0.98,1.00]				
dN=[73,55,80,68,87,95,131,133,200]				
errorN=[8.54,7.41,8.94,8.24,9.32,9.74,11.44,11.53,14.14]				
xval=np.array(sinus)				
				
yval=np.array(dN)				
errorbars=np.array(errorN)				
slope,intercept,rvalue,pvalue,stderr=linregress(xval,yval)				
fit=np.polyfit(xval,yval,1)				
bfl=np.poly1d(fit)				
plt.errorbar(xval,yval,yerr=errorbars,linestyle="None")				
				
plt.scatter(xval,yval)				
plt.plot(xval,bfl(xval))				
plt.errorbar(xval,yval,yerr=errorbars,color="b",fmt="o")				
plt.title("sin(theta/2)vs.dNGraph")				
plt.xlabel("sin(theta/2)")				
plt.ylabel("dN")				
plt.show()				
print(slope)				
print(stderr)				
x = []				
y = []				
plt.show()				