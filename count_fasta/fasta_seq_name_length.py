# Counts the number of fasta sequences and cumulative sequence length
# in a specified file, as well as individual sequence lengths.
# Fasta sequences should be continuous, not new-line separated.
# Tab-delimited table is returned for easy export

import sys

# error message if no fasta file specified
if (len(sys.argv) != 2):
	print("USAGE: one file argument required")
	sys.exit()

fasta_file = open(sys.argv[1])	
#fasta_file = open("small.fasta")	# used for debugging	


# make list of strings, separated by "\n'," corresponding to all file lines
line_list = fasta_file.readlines()
fasta_file.close()

# initialize lists for storing individual seq names and lengths
names_list = []
lengths_list = []

line_counter = 0
base_counter = 0
for line in line_list:
	if (line[0] == ">"):
		line_name = line.strip()	# removes "\n"
		line_counter += 1
		# could use here rstrip() to remove \n from line end
		names_list.append(line_name)
	else:
		current_line_length = len(line) - 1
		base_counter += current_line_length
		lengths_list.append(str(current_line_length))

# print file totals; replace sys.argv[1] with fasta_file.name for debugging
print("File", sys.argv[1], "contains", line_counter, 
	"lines, and", base_counter, "nuncleotides in total")

print("Sequence ID\tBases")
for n,l in zip(names_list, lengths_list):
	print(n + "\t" + l)

