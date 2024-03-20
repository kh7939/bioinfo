#GC content = the number of G & C / length of a DNA string

#open result files (readlines will return a list of every single line with \n)

def read_file_into_list(file):
    return [content.strip() for content in open(file,"r").readlines()]

def gc_content(DNA):
    total_GC = 0
    for i in DNA:
        if i == "G" or i == "C":
            total_GC += 1
    return round(total_GC / len(DNA) * 100, 6)

def dictionary(result):
    dictionary = {}
    for line in read_file_into_list(result):
        if line.startswith(">"):
            patient_case = line
            dictionary[patient_case] = ""
        else:
            dictionary[patient_case] += line
    dic_with_percentage = {case:gc_content(GC) for (case, GC) in dictionary.items()}
    return dic_with_percentage

# now going to find max gc content with key from the dictionary
# max function can have 'key=condition' that will find max value based on the condition
# {dictionary}.get(key) will display a value of the key 

print(max(dictionary('rosalind_gc.txt'), key=dictionary('rosalind_gc.txt').get)[1:]+'\n'+ str(max(dictionary('rosalind_gc.txt').values())))



