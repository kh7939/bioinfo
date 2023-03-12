# homozygous dominant (AA) / hetero (Aa) / homozygous recessive (aa)
# k = homo_D  / m = hetero  / n = homo_R

homo_D = 20
hetero = 16
homo_R = 18

total = homo_D + hetero + homo_R

def total_cases(k,m,n):
    total_cases = int()
    for i in range((k+m+n)-1):
        x = (k+m+n) - i
        total_cases += (x-1)
    return total_cases * 4
#total_cases * 4, why? because of punnett square

def homo_D_and_any(k):
    homo_D_cases = int()
    for i in range(k):
        homo_D_cases += ((total-1)-i)
    return homo_D_cases * 4
#homo_D_cases * 4, why? because of all offsprings will be dominant based on punnett square

def hetero_hetero(m):
    hetero_cases = int()
    for i in range(m-1):
        x = m - i
        hetero_cases += (x-1)
    return hetero_cases * 3
#hetero_cases * 3, why? because -> [Yy] & [Yy] = [YY, Yy, yY, yy]

def hetero_and_homo_R(m, n):
    cases = m * n
    return cases * 2
#hetero_and_homo_R * 2, why? because -> [Yy] & [yy] = [Yy, Yy, yy, yy]

#no need to consider homo_R & homo_R, why? becaues that will not yield any dominant phenotype

final_probability = str((homo_D_and_any(homo_D) + hetero_hetero(hetero) + hetero_and_homo_R(hetero, homo_R))/total_cases(homo_D,hetero,homo_R))
print('Final probability :', final_probability[:7])
