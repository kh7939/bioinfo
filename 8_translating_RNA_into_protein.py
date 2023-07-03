from textwrap import wrap

codons = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
        "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
        "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
        "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
        "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
        "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
        "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
        "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
        "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
        "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
        "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
        "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
        "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
        "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
        "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
        "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

# using textwrap method
# consider 'Stop' condon in real world : possibly if condons == "Stop" break
def codons_textwrap(dna):
    protein = []
    wrap_txt = wrap(dna,3)

    for i in range(len(wrap_txt)):
        if codons[wrap_txt[i]] != "Stop"    
            protein.append(codons[wrap_txt[i]])
    return "".join(protein)        

print(codons_textwrap("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))

# using slicing method
# consider 'Stop' condon in real world : possibly if condons == "Stop" break
def codons_slicing(dna):
    setofthree = []
    protein = []
    for i in range(0, len(dna), 3):
        setofthree.append(dna[i:i+3])
    for i in range(len(setofthree)):
        if codons[setofthree[i]] != "Stop":
            protein.append(codons[setofthree[i]])
    return "".join(protein)
print(codons_slicing("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))

# using slicing take way shorter time than wrap function

