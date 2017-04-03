import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

f1 = open(file_name1, "r")
f2 = open(file_name2, "r")

int1 = int(f1.readline().strip())
int2 = int(f2.readline().strip())

if (int1 < int2):
	print(int1, "+", int2, "=", int1+int2)
else:
	print(int1, "*", int2, "=", int1*int2)