import sys

base = sys.argv[1].upper()
sequence = sys.argv[2].upper()


# counter = 0

# for nucleotide in length(sequence):
# 	if sequence[nucleotide] == base:
# 		counter = counter + 1
# 	else:
# 		counter = counter

# print(counter)

counter = sequence.count(base)

print("base", base, "occurs exactly", counter, 
	"times in", sequence)

