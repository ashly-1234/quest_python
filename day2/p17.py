# 2. Find biggest digit in a number
number = input("Enter a number: ")  # Take input from the user
                                    #input() always take as string
max_digit = 0

# Iterate through each digit in the number
for digit in number:                #for i in range..   .The number inputed is of string type,we can take i as digit and range as number
    if int(digit) > max_digit:
        max_digit = int(digit)

print("The biggest digit is:", max_digit)
