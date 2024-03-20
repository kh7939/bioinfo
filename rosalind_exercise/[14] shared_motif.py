# opening FASTA file and read results by cases
def read_file(file):
    f = open(file, 'r')
    FASTA_list = [line.strip() for line in f.readlines()]
    dic = {}
    for i in FASTA_list:
        if i.startswith(">"):
            line = i
            dic[line] = ""
        else:
            dic[line] += i
    return [value for key, value in dic.items()]
Seqs = read_file('rosalind_lcsm.txt')

#Arrange Seqs by their length becuase the shared motif can not be 
#longer than the shortest sequence.

ShortestSeq = min(Seqs, key=len)

#slice the first seqcuence which is the shortest from the longest slice to the shortest
# ex) given sequence = "AGCTGTC"
# AGCTGTC, GCTGTC, AGCTGT, CTGTC, GCTGT, AGCTG and so on
for i in range(len(ShortestSeq)):
        slidingWindow = len(ShortestSeq) - i
        for j in range(len(ShortestSeq)-slidingWindow+1):
                Motif = ShortestSeq[0+j:slidingWindow+j]
                counter = 0
                for seq in Seqs:
                     if Motif not in seq:
                        break
                     else:
                        counter = counter + 1
                     if counter == len(Seqs):
                        print("The longest Motif :", Motif)
                        exit()
