text = input("Enter a string: ")
char = input("Enter a character: ")

position = text.rfind(char)

if position != -1:
    print("Last occurrence is at position", position)
else:
    print("Character not found")
