import sys
import re

seq_file = open(sys.argv[1], "r")
seq = seq_file.read()

seq_query = (sys.argv[2]).upper()

finder_result = seq.count(seq_query)

# gives indices where substring was found
appearances = [m.start() for m in re.finditer(seq_query, seq)]

if finder_result > 0:
	print(seq_query, "is present", finder_result, 
		"times, at positions:", appearances)
else:
	print(seq_query, "is absent")


#print(seq_query, seq, finder_result)
