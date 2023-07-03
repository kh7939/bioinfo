import math
import itertools

def total_perm(n):
    total = math.perm(n, n)
    return total
print(total_perm(5), end='')

def all_possible_sets(n):
    temp = itertools.permutations(range(1,n+1))
    for i in temp:
        print('')
        for j in i:
            print(j, end=' ')
    return ''

print(all_possible_sets(5))

# Permuntation - AB != BA (2 counts) AB is different from BA, the order matters
# Combination  - AB = BA (1 count) AB is the same as BA, the order does not matter
