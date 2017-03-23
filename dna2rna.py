import sys

dna_input = sys.argv[1]

rna_output = dna_input.replace("T", "U")

print("DNA input:", dna_input, "\nRNA output:", rna_output)

