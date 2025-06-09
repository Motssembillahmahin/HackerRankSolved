def birthday(s, d, m):

    count = 0
    for i in range(len(s) - m + 1):
        segment = s[i:i+m]
        if sum(segment) == d:
            count +=1
    return count