num = input("Enter a number: ")

for digit in "0123456789":
    count = num.count(digit)

    if count > 0:
        print(digit, ":", count)
