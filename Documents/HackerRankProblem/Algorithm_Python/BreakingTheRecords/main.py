
def breakingRecords(scores):
    # Write your code here
    max_pointer = scores[0]
    min_pointer = scores[0]
    max_counter = 0
    min_counter = 0
    for score in scores:
        if score > max_pointer:
            max_pointer = score
            max_counter += 1
        elif score < min_pointer:
            min_pointer = score
            min_counter += 1
    return [max_counter, min_counter]

print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]
))