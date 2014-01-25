#this module will ineterpolate the DMM function in order to use in EinsteinRad

from scipy import interpolate
from numpy import arange
import math

def Original(DMMlog):
	M1log = 11.899
	mM0 = .02817
	B = 1
	y = .6
#These constants are approximatley true, and are taken from a paper that i've got somewhere...

	denom = pow(10,(DMMlog-M1log)*-B) + pow(10,(DMMlog-M1log)*y)
	num = 2*mM0*10**DMMlog
	return math.log(num/denom, 10)


SolarMass = [] #the x part of interpolate function
DarkMatterMass = arange(10, 18, .0001) #the y part
#both of the above tables are log base 10

for dmm  in  DarkMatterMass: 
# The arange above was taken from the range we had in the output file;
#I am unsure of the stepsize
	SolarMass.append(Original(dmm))

DMMfromSMM = interpolate.interp1d(SolarMass, DarkMatterMass)

