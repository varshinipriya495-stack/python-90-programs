numbers = [10, 20, 10, 30, 20, 10]

for num in set(numbers):
    count = numbers.count(num)

    if count > 1:
        print(num, ":", count)
