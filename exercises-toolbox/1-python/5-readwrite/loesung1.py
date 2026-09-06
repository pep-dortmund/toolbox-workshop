# begin solution
import sys

if len(sys.argv) > 1:  # check if a document name is given
    filename = sys.argv[1]  # get the filename
else:
    filename = "test.txt"

with open(filename) as f:  # open the file given by the filename
    print(f.read())  # read the file and print it
# end solution
