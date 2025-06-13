from itertools import product
x = int(input())
y = int(input())
z = int(input())
n = int(input())

ranges = [range(x+1), range(y+1), range(z+1)]

permutation = [list(p) for p in product(*ranges)]

output = [p for p in permutation if sum(p) != n]

print(output)