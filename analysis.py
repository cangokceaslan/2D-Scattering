from scipy.stats import linregress
import matplotlib.pyplot as mt
import math
import numpy as np
import statistics as st
datax = [20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340]
data = [43,23,25,32,46,55,55,72,73,92,73,56,37,54,33,26,16]
datax_symmetric = [20,40,60,80,100,120,140,160,180]
sin_symmetric = []
errorbars = []
symmetric = []
errorbars_symmetric = []
for i in range(len(data)):
    errorbars.append(math.sqrt(data[i]))
for k in range(8):
    symmetric.append(data[k]+data[16-k])
    errorbars_symmetric.append(math.sqrt((data[k])+(data[16-k])))
symmetric.append(data[8]*2)
errorbars_symmetric.append(math.sqrt((data[8])+(data[8])))
for l in range(len(symmetric)):
    sin_symmetric.append(np.sin(math.radians(datax_symmetric[l] / 2)))
sine = np.array(sin_symmetric)
error = np.array(errorbars_symmetric)
dNarr = np.array(symmetric)
slope,intercept,rvalue,pvalue,stderr=linregress(sine,dNarr)		
fit=np.polyfit(sine,dNarr,1)
bfl=np.poly1d(fit)
mt.errorbar(sine,dNarr,yerr=errorbars_symmetric,linestyle="None",color="red") #this is the error bar on linefit of sinus
mt.legend("Error bars")
mt.scatter(sine,dNarr, color="red") #this is the points for symmetric symmetric summation
mt.legend("Sinus function")
mt.plot(sine,bfl(sine),color="green") #this is the fitting symmetric summation plot
mt.show()
chi_squared = np.sum((np.polyval(fit, sine) - dNarr) ** 2) #Chi of line fit
dNi = sum(symmetric) #Total of Symmetric Summation
stDni = st.stdev(symmetric) #Standard Deviation of Symmetric Summation
mt.title("Theta vs dN")				
mt.xlabel("Theta")				
mt.ylabel("dN")	
#mt.bar(datax,data,width=19,align='center',yerr=errorbars,color="gray") #this is the plot of real data we took from the paper
#mt.bar(datax_symmetric,symmetric,width=19,align='center',yerr=errorbars_symmetric,color="green") #this is the data for symmetric summation
