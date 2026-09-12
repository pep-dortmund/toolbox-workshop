# begin solution
# open the file "test.txt" in write-mode
# after the with-block, the file is closed again
with open("test.txt", "w") as f:
    f.write(str(42))
# end solution
