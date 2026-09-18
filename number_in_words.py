num = int(input("Enter a number (0-999): "))

ones = ["Zero", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"]

if num < 10:
    print(ones[num])

elif num < 20:
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    print(teens[num - 10])

else:
    tens = ["", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if num < 100:
        print(tens[num // 10], ones[num % 10])
    else:
        print(ones[num // 100], "Hundred")
