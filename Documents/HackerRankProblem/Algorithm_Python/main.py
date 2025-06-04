def miniMaxSum(arr):
    sum = []
    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            if i!=j:
                total += arr[j]
        sum.append(total)

        min_sum = sum[0]
        max_sum = sum[0]

        for i in sum[1:]:
            if i < min_sum:
                min_sum = i
            if i > max_sum:
                max_sum = i

    print(min_sum, max_sum)



miniMaxSum([1, 2, 3, 4, 5])