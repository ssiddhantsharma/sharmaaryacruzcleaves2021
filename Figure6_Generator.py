import matplotlib.pyplot as plt
import math
import re 
import sys
import glob
import os
import os.path
import numpy as np
import matplotlib.colors as mcolors

molecules = open('type_1_gephi.csv','r')
lines = molecules.readlines()
counter = 0
#print('lines'+str(lines))
with open('imagen.csv', 'a') as the_file:
	the_file.write("Id,image"+'\n') 	
	for line in lines[1:]:
		counter +=1
		line=line.rstrip('\n')
		line=line.split('\t')
		if line[1]!="2":
			print(line[0])
			code = "obabel -:"+"'"+line[0]+"'"+" -xb none -O "+"'"+line[0]+'.svg'+"'"
			print(code)
			os.system(code)
			the_file.write(line[0]+","+line[0]+'.svg'+'\n') 
