def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    for i in apples:
        if s <= a + i <= t:
            apple_count += 1

    orange_count = 0
    for i in oranges:
        if s <= b + i <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


