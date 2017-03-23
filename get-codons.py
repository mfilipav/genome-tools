# Reads first cmd line argument as DNA sequence, second argument as the readframe (0, 1 or 2)
# Returns a codon sequence in triplet characters at a given frame

import sys

sequence = (sys.argv[1]).upper()
frame = int(sys.argv[2])

#for i in range(len(sequence)-2):
for i in range(frame, len(sequence) - 2, 3):	# from 0 to length-2, update i by 3
	
	print(sequence[i:i+3])					# prints in new line
	#print(sequence[i:i+3], end=" ")		# prints in same line separated by spaces
