# 8. Count the number of Prime digits in a number
number = input("Enter a number: ")  # Take input from the user
prime_digits = {'2', '3', '5', '7'}  # Set of prime digits
count = 0

# Iterate through each digit in the number
for digit in number:
    if digit in prime_digits:
        count += 1

print("Number of prime digits:", count)

