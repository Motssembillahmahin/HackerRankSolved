from itertools import combinations


n = int(input())
lst = input().split()
k = int(input())

comb_list = list(combinations(lst, k))

count_with_a = 0

for tup in comb_list:
    if 'a' in tup:
        count_with_a += 1

# Total combinations
total = len(comb_list)

# Probability
probability = count_with_a / total

print(f"{probability:.4f}")

