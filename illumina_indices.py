"""
Returns the indices of user specified Illumina RNA PCR Index Primers (RPI)
"""

import sys

# error message if no fasta file specified
if (len(sys.argv) < 2):
	print("USAGE ERROR: you forgot to enter indices!", 
		"\nFor example, to get seqs for indices 2, 5 and 10, input them like this:",
		"\nillumina_indices.py 2 5 10")
	sys.exit()

# grabs all user supplied indices into a list, converts to int
indices = sys.argv[1:]
indices = list(map(int, indices))

seqs = {1: 'ATCACG', 
		2: 'CGATGT', 
		3: 'TTAGGC', 
		4: 'TGACCA', 
		5: 'ACAGTG', 
		6: 'GCCAAT', 
		7: 'CAGATC', 
		8: 'ACTTGA', 
		9: 'GATCAG', 
		10: 'TAGCTT', 
		11: 'GGCTAC', 
		12: 'CTTGTA', 
		13: 'AGTCAA', 
		14: 'AGTTCC', 
		15: 'ATGTCA', 
		16: 'CCGTCC', 
		17: 'GTAGAG', 
		18: 'GTCCGC', 
		19: 'GTGAAA', 
		20: 'GTGGCC', 
		21: 'GTTTCG', 
		22: 'CGTACG', 
		23: 'GAGTGG', 
		24: 'GGTAGC', 
		25: 'ACTGAT', 
		26: 'ATGAGC', 
		27: 'ATTCCT', 
		28: 'CAAAAG', 
		29: 'CAACTA', 
		30: 'CACCGG'}

print("Specified Illumina i7 index values are:")
for i in indices:
	print(i, seqs[i])

print("Copy-paste ready format:")
for i in indices:
	print(seqs[i])
