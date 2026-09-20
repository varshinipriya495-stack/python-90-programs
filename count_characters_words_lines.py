file = open("sample.txt", "r")

data = file.read()

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Characters =", characters)
print("Words =", words)
print("Lines =", lines)

file.close()
