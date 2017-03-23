# Tm is calculated for a given primer DNA sequence

import sys

seq = (sys.argv[1]).upper()

print(seq)

number_at = seq.count("A") + seq.count("T")
number_gc = seq.count("G") + seq.count("C")

melt_temp = 2*number_at + 4*number_gc

print(melt_temp, "degrees C")