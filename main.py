print("Program starting.")
print()
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))
print()

steps = 0
current = number

while current >= 10:
    digits = [int(digit) for digit in str(current)]
    result = 1

    for digit in digits:
        result *= digit

    print(" * ".join(str(digit) for digit in digits) + " = " + str(result))

    current = result
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")