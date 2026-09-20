def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if is_prime(num):
        print(num)
