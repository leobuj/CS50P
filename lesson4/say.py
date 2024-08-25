# Let's write our own library, 'sayings.py', and use some code written on
# that file within this one

import sys

# import the specific function we're gonna use
from sayings import hello

# require a single command line arg to be inputted
if len(sys.argv) != 2:
    sys.exit("Please input a single argument")

hello(sys.argv[1])