if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # arr = [[10, 20, 30], [5, 10, 15], [25, 35, 45], [0, 0, 0], [100, 200, 300]]

    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(' '.join(map(str, row)))



