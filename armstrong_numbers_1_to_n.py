n = int(input("Enter n: "))

for num in range(1, n + 1):
    original = num
    total = 0

    while num != 0:
        digit = num % 10
        total = total + digit ** 3
        num = num // 10

    if total == original:
        print(original)
