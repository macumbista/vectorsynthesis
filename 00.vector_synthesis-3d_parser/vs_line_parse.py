
import sys
import fileinput
import re
import csv
from itertools import izip



# format into list of tuples
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace(' ', ','))  # replace ' ' and write ','
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace('"', ''))  # replace '"' and write None   
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace(':', '='))  # replace ':' and write '='   
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace('{', '('))  # replace '{' and write'('
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace('}', '),'))  # replace '}' and write ')'
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace(',]', ']'))  # replace ',]' and write ']' - error correct
for i, line in enumerate(fileinput.input('lines_vertices.py', inplace=1)):
    sys.stdout.write(line.replace(',[', '['))  # replace ',[' and write '[' - error correct
    

from lines_vertices import *

linenos=[x[0] for x in lines]
xpoints=[x[0] for x in vertices]
ypoints=[x[1] for x in vertices]
zpoints=[x[2] for x in vertices]

xpoints_ord=[]
ypoints_ord=[]
zpoints_ord=[]


for i in range(len(linenos)):
	xpoints_ord.append(xpoints[int(linenos[i])])
	ypoints_ord.append(ypoints[int(linenos[i])])
	zpoints_ord.append(zpoints[int(linenos[i])])
	
print len(linenos)


with open('xvert.txt', 'wb') as f:
    for item in xpoints_ord:
    	print>>f,item
    


with open('yvert.txt', 'wb') as f:
    for item in ypoints_ord:
    	print>>f,item
    
with open('zvert.txt', 'wb') as f:
    for item in zpoints_ord:
    	print>>f,item


