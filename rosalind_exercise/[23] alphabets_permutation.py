f = open("rosalind_lexf.txt","r")
content = [lines.strip() for lines in f.readlines()]

k = int(content[1])
str = content[0]
alphabet = str.split()
k_mer = alphabet

for  l in range(k-1):
    k_mer =  [i+j for i in alphabet for j in k_mer]

for i in k_mer:
    print(i)
