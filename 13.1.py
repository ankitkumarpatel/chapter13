# ex 13.1

import string

fin= open("bookzzz.txt")

for line in fin:

   for word in line.split():
       # line= line.strip(string.punctuation+string.whitespace+" ")
       # word= line.strip(string.punctuation+sring.whitespace) 
       word= word.strip(string.punctuation+string.whitespace)
       print(word)
