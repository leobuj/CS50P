# We can actually receive arguments straight from the command line
# instead of waiting on the user to input args during runtime.
# This can speed things up sometimes.

import sys

# Let's skip the building up to it, and write code that
# is exhaustive and does not crack to zero args or too little args.
print("The name of this file is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few args")
elif len(sys.argv) > 2:
    sys.exit("Too many args!")

print("Hello, my name is", sys.argv[1])

# argv is simply a list, and we can adjust the code to take as many names as possibe.
# for arg in argv[1:] :
#     print("hello,", arg)

