# sudo pip install requests (requests library)
# how to scrap a website --> requests.get(links).text
import requests

dict = {}
f = open("rosalind_mprt.txt", 'r')

for lines in f.readlines():
    proteins = lines.strip()[:6]
    dict[lines.strip()] = requests.get('https://rest.uniprot.org/uniprotkb/'+proteins+'.fasta').text
    temp = dict[lines.strip()].find("\n")
    dict[lines.strip()] = dict[lines.strip()][temp+1:].replace("\n", "")

# looking for N-glycosylation motif
# The N-glycosylation motif is written as N{P}[ST]{P}.
# ex) [XY] means "either X or Y" and {X} means "any amino acid except X." 

answer = {}
for k,v in dict.items():
    answer[k] = ""
    for i in range(len(v)-4):         
      if v[i] == "N" and v[i+1] != "P" and (v[i+2] == "S" or v[i+2] == "T") and v[i+3] != "P":
        p_motifs = str(i+1) + " "
        answer[k] += p_motifs
    if answer[k] != "":
       print(k)
       print(answer[k])
    
