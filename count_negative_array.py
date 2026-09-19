numbers = [10, -5, 20, -8, 15, -3]

count = 0

for num in numbers:
    if num < 0:
        count += 1

print("Negative elements =", count)
