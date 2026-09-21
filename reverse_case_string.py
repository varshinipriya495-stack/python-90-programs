text = input("Enter a string: ")

result = ""

for char in text:
    if char.isupper():
        result = result + char.lower()
    elif char.islower():
        result = result + char.upper()
    else:
        result = result + char

print("Reverse case =", result)
