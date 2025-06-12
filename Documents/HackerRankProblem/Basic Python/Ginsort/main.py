S = input()

lowercase = sorted([ch for ch in S if ch.islower()])
uppercase = sorted([ch for ch in S if ch.isupper()])
digits = sorted([int(ch) for ch in S if ch.isdigit()])

odd_digits = sorted([str(i) for i in digits if i % 2 != 0])
even_digits = sorted([str(i) for i in digits if i % 2 == 0])

result = "".join(lowercase + uppercase + odd_digits+even_digits)
print(result)