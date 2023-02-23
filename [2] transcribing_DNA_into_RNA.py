# DNA -> RNA (transcription) (replacing 'T' into 'U')
# RNA -> protein (translation)
# using replace function

def DNA_into_RNA(DNA):
    return DNA.replace("T", "U")

print(DNA_into_RNA("GATGGAACTTGACTACGTAAATT"))
