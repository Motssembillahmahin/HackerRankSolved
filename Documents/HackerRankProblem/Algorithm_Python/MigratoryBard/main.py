# solution 1
from collections import Counter
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

# counter = Counter(arr)
# max_count = max(counter.values())
# most_frequent = [num for num, cnt in counter.items() if cnt == max_count]
# min_frequent = min(most_frequent)
# print(min_frequent)


# solution 2

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
max_count = 0

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
print(max_count)

most_frequent = []
for key in frequency:
    if frequency[key] == max_count:
        most_frequent.append(key)

min_freq = most_frequent[0]

for i in most_frequent:
    if i < min_freq:
        min_freq = i

print(most_frequent)