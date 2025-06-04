if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    result = list(sorted(set(arr), reverse= True))
    print(result[1])