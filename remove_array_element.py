numbers = [10, 20, 30, 40, 50]

position = int(input("Enter position to delete: "))

if 0 <= position < len(numbers):
    numbers.pop(position)
    print("Array after deletion =", numbers)
else:
    print("Invalid position")
