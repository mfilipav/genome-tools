# counts the number of fasta sequences in a file specified on the command line
import sys

# error message if no fasta file specified
if (len(sys.argv) != 2):
	print("USAGE: one file argument required")
	sys.exit()

fasta_file = open(sys.argv[1])

# make list of strings, separated by "\n'," corresponding to all file lines
line_list = fasta_file.readlines()
fasta_file.close()

counter = 0
for line in line_list:
	if (line[0] == ">"):
		print(line)
		counter += 1


print(sys.argv[1], "contains", counter, "lines")