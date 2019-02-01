# ex 13.1

import string

unwanted_punctuations = string.punctuation + string.whitespace 

fin= open("bookzzz.txt")

for line in fin:
   for word in line.split():
       word = word.strip(unwanted_punctuations).lower()
       print(word)

