def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    return total == num


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if is_perfect(num):
        print(num)
