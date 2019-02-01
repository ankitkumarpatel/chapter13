# ex 13.1

import string

fin= open("bookzzz.txt")

for line in fin:
    line= line.strip(string.punctuation+string.whitespace+" ")

    print(line)
