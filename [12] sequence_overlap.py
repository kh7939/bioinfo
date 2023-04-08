#when there is a length k suffix of string S that matches a length k prefix of string T
#open a result file -> find a overlp between 2 strings (front from one and back from the other)

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
    return dic

def overlaps(length):
    string_list = [value for (key, value) in read_file('rosalind_grph.txt').items()]
    string_list_swap = {values:keys[1:] for (keys, values) in read_file('rosalind_grph.txt').items()}
    result = []

    for first_string in range(len(string_list)):
        for second_string in range(len(string_list)):
            if string_list[first_string][-length:] == string_list[second_string][:length] and string_list[first_string] != string_list[second_string]:
                print(string_list_swap[string_list[first_string]], string_list_swap[string_list[second_string]])
    
overlaps(3)





