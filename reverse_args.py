# takes a list of strings as input and prints the reversed strings,
# separated by "*".
import sys

args = sys.argv[1:]

print(args)

args.reverse() 		# remember, lists are mutable, so no need to create new list.

print("*".join(args))

### fix this shitiititi