from collections import Counter



s = 'aabbccddef'
counter = Counter(s)

top_three = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]

for char, count in top_three:
    print(char, count)