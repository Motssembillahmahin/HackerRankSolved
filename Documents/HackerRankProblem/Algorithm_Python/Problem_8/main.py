


def birthdayCakeCandles(candles):
    tallest = candles[0]
    count = 0

    for i in range(len(candles)):
        if candles[i] > tallest:
            tallest = candles[i]
            count = 1
        elif candles[i] == tallest:
            count += 1
    print(count)


birthdayCakeCandles([3, 2, 1, 3])