a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)
