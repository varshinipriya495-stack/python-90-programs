text = input("Enter a string: ")

highest = 0
character = ""

for char in text:
    count = text.count(char)

    if count > highest:
        highest = count
        character = char

print("Highest frequency character =", character)
print("Frequency =", highest)
