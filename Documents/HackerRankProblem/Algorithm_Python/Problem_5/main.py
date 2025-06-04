def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0


    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos / n:.6f}")
    print(f"{neg / n:.6f}")
    print(f"{zero / n:.6f}")