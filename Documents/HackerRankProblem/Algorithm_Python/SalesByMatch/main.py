
ar = [70, 20, 20, 10, 10, 30, 50, 10, 20]


frequency =  {}

for num in ar:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

pair_count = 0
for key, value in frequency.items():
    pair_count += value // 2  

print(pair_count)