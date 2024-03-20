# A DNA string is a reverse palindrome if it is equal to its reverse complement. 
# For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

def open_file(file):
    f = open(file, 'r').readlines()
    lines = [i.strip() for i in f]
    dic = {}
    for line in lines:
        if line.startswith(">"):
            case = line
            dic[case] = ""
        else:
            dic[case] += line
    return [values for keys, values in dic.items()]

s = open_file("rosalind_revp.txt")[0]

base = {"A":"T", "T":"A", "G":"C", "C":"G"}

def reverse(dna):
    temp = str.maketrans("ATGC", "TACG")
    rs = dna.translate(temp)
    return rs[::-1]
    
def find_all_location(substring, s):
    for l in substring:
        for i in range(len(s)):
            if s[i:i+len(l)] == l:
                print(i+1, len(l))
    return
   
list = []
length = 12

# split a given string into length of 4 & 6 & 8 & 10 & 12
# and then save strings that are palidrom in the firt and last nucleotide

while length >= 4:
    for i in range(len(s)-(length-1)):
        if base[s[i:i+(length)][0]] == s[i:i+(length)][-1]:
            list.append(s[i:i+(length)])
    length = length - 2
temp =[]

# compare a reverse complement of the first half to the second half to see if they are indentical
# e.g.    a string ATCGAT, a reverse complement of the first half GAT (ATC -> TAG -> GAT)

for string in list:
    half = int(len(string)/2)
    if reverse(string[:half]) == string[half:]:
        if string not in temp:
            temp.append(string)
            
find_all_location(temp,s)

 
