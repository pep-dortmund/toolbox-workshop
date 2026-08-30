# begin solution
import sys

if len(sys.argv) > 1:  # check if a document name is given
    filename = sys.argv[1]  # get the filename
else:
    filename = "test.txt"

with open(filename, "r") as f:  # open the filename in read-mode
    print(f.read())  # read the file and print it
# end solution
