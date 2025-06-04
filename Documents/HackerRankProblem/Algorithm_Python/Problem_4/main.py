def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n - 1 - i]

    return abs(primary_diagonal - secondary_diagonal)


diagonalDifference( [[11, 2, 4], [4, 5, 6], [10, 8, -12]])