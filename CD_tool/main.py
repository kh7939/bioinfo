from DNAToolkit import *
import random
from utilities import colored


rndDNAStr = "".join([random.choice(Nucleotides) for nuc in range(77)])

DNAstr = validateSeq(rndDNAStr)

print(f"Sequence: {colored(DNAstr)}\n")
print(f"[1] + Sequence Length: {len(DNAstr)}\n")
print(colored(f"[2] + Nueclotide Frequency: {countNucFrequency(DNAstr)}\n"))

print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAstr))}\n")
print(f"[4] + DNA String - Reverse Complement:\n\n5' {colored(DNAstr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAstr))])}")
print(f"3' {colored(reverse_complement(DNAstr)[::-1])} 5' [Complement]\n")
print(f"5' {colored(reverse_complement(DNAstr))} 3' [Rev. Complement]\n")

print(f"[5] + GC Content: {gc_content(DNAstr)}%\n")
print(f"[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAstr, k=5)}\n")

print(f"[7] + Aminoacids Sequence from DNA: {translate_seq(DNAstr, 0)}\n")
print(f'[8] + Codon frequency (L): {condon_usage(DNAstr, "L")}\n')

print("[9] + Reading_frames: ")
for frame in gen_reading_frames(DNAstr):
    print(frame)
   

#test_rf_frame = ['V', 'F', 'S', 'Q', 'S', 'H', 'N', 'R', 'R', 'M', 'V', 'P', 'S', 'S', 'N', 'V', 'Y', 'S', 'S', 'L', 'G', 'S', 'G', 'T', 'D', 'S', 'E', 'N', 'R', 'G', 'C', 'S', '_', 'Y', 'N', 'R', 'S', 'L', 'G', 'D', 'L', 'Y', 'T', 'E', 'L', 'M', 'F', 'E', 'A', 'L', 'H', 'P', 'T', 'L', 'I', 'A', 'Y', 'H', '_', 'E', 'D', 'N', 'H', 'I', 'S', 'S', 'E', 'Q', 'Y', 'Q', 'S', 'L', 'R', 'P', 'V', 'E', 'I', 'V', 'E', 'P', 'R', 'D', 'I', 'S', 'G', 'S', 'G', 'I', 'C', 'M', 'V', 'S', 'R', 'P', 'M', 'F', 'C', '_', 'K', 'T']
#print(proteins_from_rf(test_rf_frame))

print('\n[10] + All prots in 6 reading frames:')
for prot in all_porteins_from_orfs(DNAstr, 0, 0, True):
    print(f'{prot}')
