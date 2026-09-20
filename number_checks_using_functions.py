def is_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count == 2


def is_armstrong(num):
    original = num
    total = 0

    while num != 0:
        digit = num % 10
        total = total + digit ** 3
        num = num // 10

    return total == original


def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    return total == num


num = int(input("Enter a number: "))

print("Prime:", is_prime(num))
print("Armstrong:", is_armstrong(num))
print("Perfect:", is_perfect(num))
