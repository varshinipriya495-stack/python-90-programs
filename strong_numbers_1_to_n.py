n = int(input("Enter n: "))

for num in range(1, n + 1):
    original = num
    total = 0

    while num != 0:
        digit = num % 10

        factorial = 1
        for i in range(1, digit + 1):
            factorial = factorial * i

        total = total + factorial
        num = num // 10

    if total == original:
        print(original)
