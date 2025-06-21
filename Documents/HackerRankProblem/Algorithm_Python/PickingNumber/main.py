def pickingNumbers(a):
    max_len = 0
    unique_values = set(a)

    for num in unique_values:
        count = 0
        for val in a:
            if val == num or val == num + 1:
                count += 1
        max_len = max(max_len, count)

    return max_len



