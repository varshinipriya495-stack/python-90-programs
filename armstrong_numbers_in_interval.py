def is_armstrong(num):
    original = num
    total = 0

    while num != 0:
        digit = num % 10
        total = total + digit ** 3
        num = num // 10

    return total == original


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
