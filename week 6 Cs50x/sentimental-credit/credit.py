number = input("Number: ")

if len(number) == 15 and (number[:2] == "34" or number[:2] == "37"):
    print("AMEX")

elif len(number) == 16 and number[:2] in "5152535455":
    print("MASTERCARD")

elif 13 <= len(number) <= 16 and number[0] == "4":
    print("VISA")

else:
    print("INVALID")