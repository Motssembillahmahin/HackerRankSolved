import math
def viralAdvertising(n):
    # Write your code here
    count = 0
    temp_shared = 5
    for _ in range(n):
        temp = temp_shared // 2
        count += temp
        temp_shared = temp * 3
    return count

print(viralAdvertising(5))

