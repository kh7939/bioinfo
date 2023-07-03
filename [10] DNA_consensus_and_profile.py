# It will list DNA strings as rows
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

#print(open_file('rosalind_cons.txt'))

# It will count DNA strings as column;
# when you arrange multiple stirngs that are the same length
# it will count bases by columns instead of rows.
def count_matrix(list):
    n = len(list[0])
    dic = {"A" : [0] * n,
           "C" : [0] * n,
           "G" : [0] * n,
           "T" : [0] * n}
    for i in list:
        for x, y in enumerate(i):
            dic[y][x] += 1
    return dic

result = []
x = count_matrix(open_file('rosalind_cons.txt'))

for position in range(len(open_file('rosalind_cons.txt')[0])): 
    max_count = 0
    max_n = str()
    for n in ["A","C","G","T"]:
        count = x[n][position]
        if count > max_count:
            max_count = count
            max_n = n
    result.append(max_n)
print("".join(result))

#Below is just to display count_matrix in a format that Rosalind asks.

list_a = []
list_c = []
list_g = []
list_t = []

for i in x:
    if i == "A":
        for a in x[i]:
            list_a.append(str(a))
    elif i == "C":
        for c in x[i]:
            list_c.append(str(c))
    elif i == "G":
        for g in x[i]:
            list_g.append(str(g))
    else:
        for t in x[i]:
            list_t.append(str(t))

print("A:", " ".join(list_a),"\n"
     "C:", " ".join(list_c),"\n"
      "G:", " ".join(list_g),"\n"
      "T:", " ".join(list_t))



