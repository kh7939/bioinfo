#1.AA-AA = all Dominant
#2.AA-Aa = all Dominant
#3.AA-aa = all Dominant
#4.Aa-Aa = 3/4 Dominant
#5.Aa-aa = 1/2 Dominant
#6.aa-aa = 0 Dominant

# list dominant probability in order as above
D_probability = [1, 1, 1, 0.75, 0.5, 0]

given = open("rosalind_iev.txt", "r").readline().strip()
list = given.split(" ")
print(list)

def expected_offsprings():
  result = []
  for i in range(len(list)):
    result.append(int(list[i])*D_probability[i]*2)
  return sum(result)

print(expected_offsprings())
