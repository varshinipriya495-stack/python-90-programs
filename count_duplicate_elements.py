numbers = [10, 20, 10, 30, 20, 10]

for num in set(numbers):
    if numbers.count(num) > 1:
        print(num, ":", numbers.count(num))
