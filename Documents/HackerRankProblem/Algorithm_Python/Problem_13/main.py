import math

def encryption(s):
    s = s.replace(' ', '')
    rows = math.floor(math.sqrt(len(s)))
    cols = math.ceil(math.sqrt(len(s)))

    if rows * cols < len(s):
        rows += 1

    matrix = [s[i:i+cols] for i in range(0, len(s), cols)]
    print(matrix)
    result = ''
    for i in range(cols):
        for row in matrix:
            if i < len(row):
                result += row[i]
        result += ' '
    return result.strip()

print(encryption("This is mahin hwo to deal with it"))
