#using dictionary

def count_DNA_dict(DNA):
    d = {}
    for i in DNA:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print("[1] using dictionary :", count_DNA_dict("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" * 30))

#using collections and Counter

from collections import Counter

def count_DNA_Counter(DNA):
    return Counter(DNA)

print("[2] using Counter :", count_DNA_Counter("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" * 74))
