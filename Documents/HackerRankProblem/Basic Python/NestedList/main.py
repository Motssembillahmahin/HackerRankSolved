records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

unique_scores = sorted(set(score for name, score in records))
print(unique_scores)
if len(unique_scores) >= 1:
    second_lowest = unique_scores[1] if len(unique_scores) > 1 else unique_scores[0]
    names = sorted(name for name, score in records if score == second_lowest)
    print("\n".join(names))
else:
    print("Not enough distinct scores to find the second lowest.")
