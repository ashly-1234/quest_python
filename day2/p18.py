# 3. Find 2nd smallest digit in a number
number = input("Enter a number: ")  # Take input from the user

# Convert the number to a set of digits to remove duplicates and then sort it
unique_digits = sorted(set(number))

# Check if there are at least two unique digits
if len(unique_digits) < 2:
    print("There is no second smallest digit.")
else:
    second_smallest_digit = unique_digits[1]  # Get the second smallest digit
    print("The second smallest digit is:", second_smallest_digit)
