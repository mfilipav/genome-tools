# reads ith through jth lines from a file
# bla

import sys
open_file = open(sys.argv[3])

counter = int(sys.argv[1])
while counter <= int(sys.argv[2]):
	print(open_file.readline(), end = "")
	counter += 1
open_file.close()
