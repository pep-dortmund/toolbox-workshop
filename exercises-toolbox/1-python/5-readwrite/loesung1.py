# begin solution
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "test.txt"

with open(filename, "r") as f:
    print(f.read())
# end solution
