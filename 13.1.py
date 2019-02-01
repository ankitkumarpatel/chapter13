# ex 13.1

import string



fin= open("bookzzz.txt")

for line in fin:
   for word in line.split():
       word= word.strip(string.punctuation+string.whitespace).lower()
       print(word)

