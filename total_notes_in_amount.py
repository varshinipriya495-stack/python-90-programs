amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

for note in notes:
    count = amount // note
    if count > 0:
        print(note, ":", count)
        total_notes += count
        amount = amount % note

print("Total number of notes =", total_notes)
