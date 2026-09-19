text = input("Enter a string: ")

lowest = len(text)
character = ""

for char in text:
    count = text.count(char)

    if count < lowest:
        lowest = count
        character = char

print("Lowest frequency character =", character)
print("Frequency =", lowest)
