# 1. Find sum of Even placed digits in a number
number = input("Enter a number: ")  # Take input from the user
even_placed_digits_sum = 0

# Iterate through the digits at even indices (0-based)
for index in range(0, len(number), 2):
    even_placed_digits_sum += int(number[index])

print("Sum of even-placed digits:", even_placed_digits_sum)
