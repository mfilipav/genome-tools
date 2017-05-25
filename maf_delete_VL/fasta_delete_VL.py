import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC


if len(sys.argv) < 1:
	print("Usage: at least one argument expected. Check if you specified .fasta file")
	sys.exit()

fasta_file = sys.argv[1]
tak424 = "CGTTCAGAGTTCTACAGTCCGACGATC"
lox511 = "ATAACTTCGTATAATGTATACTATACGAAGTTAT"
fid = "HHHHACHHHHACHHHNGCAG"
lox_tail = "CCTCGAGCGGTACC"


# read in fasta sequences into Seq object
fasta_sequences = SeqIO.parse(open(fasta_file), "fasta")
new_sequences_list = []

# find VL beginning and ending indeces, cut out VL,
# write out new .fasta file
for sequence in fasta_sequences:
	print(">"+sequence.id, "\nSeq length:", len(sequence.seq))

	# sequence.seq is the fasta sequence, must specify
	# .seq or .id searchable object	
	first_cut = sequence.seq.find(tak424) + len(tak424) + len(fid)
	print("1st cut index:", first_cut)
	
	second_cut = sequence.seq.find(lox511) + len(lox511) + len(lox_tail)
	print("2nd cut index:", second_cut)

	cut_sequence = str(sequence.seq[0:first_cut] + "--" 
						+ sequence.seq[second_cut:])
	print("After removing VL:", cut_sequence)
	print()

	new_sequences_list.append(SeqRecord(Seq(cut_sequence), 
										id=sequence.id, 
										description="VL region removed"))						

SeqIO.write(new_sequences_list, "test_seq_deleted_VL.fasta", "fasta")
