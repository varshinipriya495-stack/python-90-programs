text = input("Enter a string: ")
char = input("Enter a character: ")

for i in range(len(text)):
    if text[i] == char:
        print("Character found at position", i)
