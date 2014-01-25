## Strong Gravitational Lens search in SQL Databases

The python code and SQL queries in this repository are designed to find candidate strong gravitational lenses in astronomical SQL databases. The basic idea is dimple. First, find candidate lensing galaxies. Second, search around these possible lenses for blue neighbors. Third, Python code predicts an Einstein radius given measured properties of the candidate lensing galaxy such as stellar mass (which we convert to a dark matter mass). If the candidate galaxy has blue neighbors at approximately the Einstein radius we consider a good strong lens candidate.

Authors: Sean McLaughlin, Robert J. Brunner

Note, the conversion between stellar mass (as measured from spectral absorption lines) and dark matter mass (or dynamical mass) was obtained from _Constraints on the Relationship between Stellar Mass and Halo Mass at Low and High Redshift_ by Benjamin P. Moster, Rachel S. Somerville, Christian Maulbetsch, Frank C. van den Bosch, Andrea V. Macciò, Thorsten Naab, and Ludwig Oser (2010, ApJ, 710, 903).

## Code Usage:

### EinsteinRad_2.py

This code computes the Einstein radius.

python EinsteinRad_2.py CSV. 

Where CSV is a csv file with columns:

objid, ra, dec, z, MinSolarMass, MaxSolarMass

in that order (though the order may not matter). 

The output is a csv with columns:

objid, ra, dec, z, maxER, minER 

where ER is the einstein radius. The output is written to 'ERoutput.csv'. 

The file, SQ15.csv in the data subdirectory is a valid example input.

### QT_2.py 
This code matches objects between two files, either using an intersection or differencing. This allows matching of lens data between files (by matching the candidate lens galaxy)

python QT_2.py intersect, filename (optional knownFilename)

intersect: t, true, T, or True. If true do an intersect, otherwise it will do a subtract.
filename: the filename to read from
knownFilename: the filename to use for the known lenses. If none specified, will used "kldr9.csv"

The file kldr9_2.csv is our most recent library of known lenses to use along with SQ15.csv as a sample input.
