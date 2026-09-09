# begin solution
import sys

if len(sys.argv) > 1:  # check if a document name is given
    filename = sys.argv[1]  # get the filename
else:
    filename = "test.txt"

# the file, given by `filename`` is open inside of the `with` block
# inside of the block, it can be accessed with `f`
# after the block, the file is closed (`f.close()`)
with open(filename) as f:
    print(f.read())  # read the file and print it
# end solution
