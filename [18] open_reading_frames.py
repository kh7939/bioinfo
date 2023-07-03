dna_codons = {"TTT":"F", "CTT":"L", "ATT":"I", "GTT":"V",
        "TTC":"F", "CTC":"L", "ATC":"I", "GTC":"V",
        "TTA":"L", "CTA":"L", "ATA":"I", "GTA":"V",
        "TTG":"L", "CTG":"L", "ATG":"M", "GTG":"V",
        "TCT":"S", "CCT":"P", "ACT":"T", "GCT":"A",
        "TCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
        "TCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
        "TCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
        "TAT":"Y", "CAT":"H", "AAT":"N", "GAT":"D",
        "TAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
        "TAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
        "TAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
        "TGT":"C", "CGT":"R", "AGT":"S", "GGT":"G",
        "TGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
        "TGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
        "TGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

def open_file(file):
    f = open(file, "r")
    string = ''
    for i in f.readlines():
        if i.startswith(">"):
            continue
        else:
            string += i.strip()
    return string

def reverse_string(string):
    rstring = str.maketrans("ATCG", "TAGC")
    return string.translate(rstring)[::-1]

# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon,
# without any other stop codons in between
# Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
#ATG = M (start codon)
#TAA/TAG/TGA = stop codons
def start_stop(string):
    start=[]
    stop=[]
    for st_sp_codons in range(len(string)):
        if string[st_sp_codons:st_sp_codons+3] == "ATG":
            start.append(st_sp_codons)
        elif (string[st_sp_codons:st_sp_codons+3]=='TAA') \
            or (string[st_sp_codons:st_sp_codons+3]=='TAG') \
                or (string[st_sp_codons:st_sp_codons+3]=='TGA'):
            stop.append(st_sp_codons+3)
    fragments={}
    for i in start:
        for j in stop:
            if (j > i) and ((j-i) %3 ==0):
        	    if i not in fragments:
                        fragments[i] = j
    return [string[k:v] for k,v in fragments.items()]

temp_split_stop = ''
for protein in start_stop(open_file('rosalind_orf.txt')):
	for codons in range(0,len(protein),3):
    	 temp_split_stop += dna_codons[protein[codons:codons+3]]
for protein in start_stop(reverse_string(open_file('rosalind_orf.txt'))):
    for codons in range(0,len(protein),3):
    	 temp_split_stop += dna_codons[protein[codons:codons+3]]
         
#*set(iterable) = remove duplicate
for i in [*set(temp_split_stop.split("Stop"))]:
    if i != "":
        print(i)
