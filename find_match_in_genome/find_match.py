# Returns the number of lines where query [2] is found 
# in specified tab [3] of the large text file [1].
# Optional 4th argument specifies minimum repeat length [4].
# example usage: python find_match.py cfam_repmask2.txt CfERV1 11 1000

import sys
if len(sys.argv) < 4:
	print("Usage: at least three arguments expected")
	sys.exit()

open_file = open(sys.argv[1])
query = str(sys.argv[2])
tab_index = int(sys.argv[3])
repeat_length = 0
if len(sys.argv) == 5:		# if input for min repeat length is provided
	repeat_length = int(sys.argv[4])

# various counters:
line_counter = 0
find_counter = 0
for line in open_file:
	line_counter += 1

	fields = line.split("\t")
	if fields[tab_index-1] == query :
		measured_repeat_length = int(fields[7]) - int(fields[6])
		
		if measured_repeat_length >= repeat_length:
			find_counter += 1

open_file.close()

print("Query for", sys.argv[2], "is found", find_counter, 
	"times in tab", tab_index-1, "\namong", line_counter, 
	"total lines. \nMinimum genomic length filter used:", repeat_length)