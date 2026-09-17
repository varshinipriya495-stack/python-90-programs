units = int(input("Enter units: "))

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 25 + (units - 50) * 0.75
elif units <= 250:
    bill = 100 + (units - 150) * 1.20
else:
    bill = 220 + (units - 250) * 1.50

bill = bill + bill * 0.20

print("Total Electricity Bill =", bill)
