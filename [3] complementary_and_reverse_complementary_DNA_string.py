# complementary strand

def complementary_strand(DNA):
    bases = {"A":"T", "T":"A", "G":"C", "C":"G"}
    result = ""
    for i in DNA:
        result += bases[i]
    return result

print("[1] complementary strand :", complementary_strand("ACGTTCGTCAAGTCAGTCCAAGTCCGTA"))

# reverse-complementary strand

def reverse_complementary_strand(DNA):
    return complementary_strand(DNA)[::-1]

print("[2] reverse complementary strand :", reverse_complementary_strand("ACGTTCGTCAAGTCAGTCCAAGTCCGTA"))
    
