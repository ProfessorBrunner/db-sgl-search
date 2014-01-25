#this is my attempt to improve qt.py and nqt.py
#intersect is either true or false, and this determines if this search is an intersect or not
from sys import argv
import csv

if len(argv) ==3:
	script, intersect, filename = argv
	knownFilename = 'kldr9.csv'

elif len(argv) == 4:
	script, intersect, filename, knownFilename = argv

else:
	raise IOError, 'Invalid Entry'

dataReader = csv.DictReader(open(filename))
knownReader = csv.DictReader(open(knownFilename))

knownOBJIDs = set()
for line in knownReader:
	knownOBJIDs.add(line['objid'])

keys = ['objid', 'ra', 'dec'] #line.keys()
out =[ ','.join(keys)]

if intersect in ['True', 'T', 'true', 't']:
	for line in dataReader:
		if line['objid'] in knownOBJIDs:
			out.append(','.join(line[key] for key in keys))

else:
	for line in dataReader:
		if line['objid'] not in knownOBJIDs:
			out.append(','.join(line[key] for key in keys))

finalStr = '\n'.join(out)

with open('output.csv', 'w') as output:
	output.write(finalStr)
