def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result


def is_strong(num):
    original = num
    total = 0

    while num != 0:
        digit = num % 10
        total = total + factorial(digit)
        num = num // 10

    return total == original


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if is_strong(num):
        print(num)
