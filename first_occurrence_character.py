text = input("Enter a string: ")
char = input("Enter a character: ")

position = text.find(char)

if position != -1:
    print("First occurrence is at position", position)
else:
    print("Character not found")
