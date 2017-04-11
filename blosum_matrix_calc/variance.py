# reads in a specified BLOSUM score matrix from .txt, and computes
# mean and variance of scores for each Amino Acid

import sys
import numpy
file = open(sys.argv[1])
# make list of strings, separated by "\n'," corresponding to 20 aa
file_lines = file.readlines()
file.close()

aa_list = []
mean_list = []
var_list = []

for line in range(0, len(file_lines)):
	score_list = [] # list of scores for this line

	line_values_list = file_lines[line].split()

	aa_list.append(line_values_list[0])

	for value in range(1, len(line_values_list)):
		score_list.append(int(line_values_list[value]))
	
	# NUMPY magic
	mean_list.append(numpy.mean(score_list))
	var_list.append(numpy.var(score_list))


numpy_ndarray = numpy.column_stack((aa_list, numpy.around(mean_list), 
	numpy.around(var_list)))
print(numpy_ndarray)
