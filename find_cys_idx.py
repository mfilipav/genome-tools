# Reads in aa sequence string, prints the index of all Cys

import sys
import re 	# regular expressions

sequence = (sys.argv[1]).upper()

print("Position indeces for Cys residues in", sequence, " aa sequence are:")

for m in re.finditer("C", sequence):
	print(m.start(), end=" ")

print("")
