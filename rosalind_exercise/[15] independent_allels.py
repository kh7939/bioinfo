# If a person with heterozygous genotype with 2 different genes mates with any genotype,
# the probability that their offsprings will be heterozygous is always 4/16 (25%).

# given that, each couple reproduces 2 children.
import math

def hetero(gen, the_number_of_hetero):
    children_at_gen = 2**gen
    p = 0
    for i in range(1, children_at_gen + 1):
        if the_number_of_hetero == 1:
            p = 1 - (3/4)**children_at_gen
        elif i >= the_number_of_hetero:
            temp = ((1/4))**(i) * (3/4)**(children_at_gen - i) * math.comb(children_at_gen, i)
            p += temp
    return p

print(round(hetero(7, 35), 3))

# Permuntation - AB != BA (2 counts) AB is different from BA
# Combination  - AB = BA (1 count) AB is the same as BA
