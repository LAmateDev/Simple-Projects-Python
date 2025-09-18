height = int(input("Height: "))

while height < 1 or height > 8:
    height = int(input("Height: "))
for i in range(height - 1, -1, -1):
    print(" " * i, end="")
    print("#" * (height - i), end="  ")
    print("#" * (height - i))
