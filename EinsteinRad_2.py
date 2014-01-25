#This program takes a csv file as an input with min mass and max mass and redshift and returns an estimate for upper and lower einstein radius
from sys import argv
import math
from DarkMatterMass import DMMfromSMM#user function i created
from time import time
from cdistance import cdistance
import csv


if len(argv)!=2 and __name__=='__main__':
	print """
This module takes a csv as an input, of the form objid,ra,dec,z,MinSolarMass,MaxSolarMass and returns an output file "ERoutput.csv" that is of the form objid, ra, dec,ERMax, ERmin where ERmax and min are the maximum and minimum einstein radius.
In the same directory as this there should be the "DarkMatterMass.py", "CsvPull.py"and "cdistance.py" modules.
It would be pretty trivial to take the methods in those modules and compile them into this one; I intend to use those modules in other places so I made them seperately.

Email me at mclaughlin6464@gmail.com if you've got any questions.
	"""
else:

	dist = cdistance() # the cdistance module uses objects; easiest to initialize here
	def powTen(n):
		return pow(10,n) #Just a simple function to easily do scientific notation

	def DfromZ(z):
#calculate the distance from the redshift.
#I believe we need the angular diameter distance but this module does them all if need be 
		return dist.da(z)
		
	def ER(mlog, D):#formula for the einstein radius,
		return  math.sqrt(powTen(mlog-11.09)/D)*.01667 #arcminutes

	script, filename = argv
	data = csv.DictReader(open(filename))
	out= ["objid,ra,dec,maxER,minER"]
	keys = ['objid','ra','dec','z', 'minLogMass','maxLogMass']
	for line in data:
		z = float(line['z'])
		minSM = float(line['minLogMass'])
		maxSM = float(line['maxLogMass'])
		
		if any(9>SM or SM>14 for SM in (minSM, maxSM)):
		#i've run into a few problems where there were weird sizes, outside of the interpolation, so I skip em.
			continue
		#hese 3 lines are the most significant computationally.
		#average is .0003 seconds per galaxy; not much, but 10x more than any other section. 
		maxDMM = DMMfromSMM(maxSM)
		minDMM = DMMfromSMM(minSM)
		D = DfromZ(z)
#all these calls should be self explanatory
		ERmax = ER(maxDMM, D)
		ERmin = ER(minDMM, D)
		output = ','.join([line['objid'], line['ra'], line['dec'], str(ERmax), str(ERmin)])
		out.append(output)

	with open('ERoutput.csv', 'w') as ERoutput:
		ERoutput.write('\n'.join(out))
