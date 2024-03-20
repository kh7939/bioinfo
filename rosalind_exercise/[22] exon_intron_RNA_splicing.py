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

first_string = open_file("rosalind_splc.txt")[0]
the_rest = open_file("rosalind_splc.txt")[1:]

intron_out = first_string

for i in the_rest:
    intron_out = intron_out.replace(i,"")

protein = ""

for i in range(0, len(intron_out), 3):
    if dna_codons[intron_out[i:i+3]] == "Stop":
        continue
    else:
        protein += dna_codons[intron_out[i:i+3]]

print(protein)
