numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")
prime_file = open("prime.txt", "w")

for num in numbers:
    if num % 2 == 0:
        even_file.write(str(num) + "\n")
    else:
        odd_file.write(str(num) + "\n")

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        prime_file.write(str(num) + "\n")

even_file.close()
odd_file.close()
prime_file.close()

print("Numbers written to separate files")
