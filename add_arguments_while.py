# reads from console any number of integers and prints the cumulative total for
# each successive argument
import sys
counter = 0

# solution with WHILE LOOP:
i = 1	# 0th sys argument vector is <program_name>.py
while i < len(sys.argv):
	counter += int(sys.argv[i])
	print(i, "-->", counter)
	i += 1 
#print(len(sys.argv)) # if entered 3 numbers, then L = 4
print(sys.argv[0])

# # solution with FOR LOOP:
# for i in sys.argv[1:]:
# 	counter += int(i)
# 	print(counter)

print("Cumulative total is:", counter)
