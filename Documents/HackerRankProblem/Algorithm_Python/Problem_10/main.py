def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count