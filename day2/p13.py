# Program to count the number of Odd digits in a number

# Get the input number from the user
number = int(input("Enter the number that you want to count the odd digits: "))

# Copy the input number to a temporary variable
temp_number = number

# Initialize a counter for odd digits
odd_count = 0

# Use a while loop to iterate through each digit of the number
while number > 0:
    # Extract the last digit of the number
    digit = number % 10
    
    # Check if the digit is odd
    if digit % 2 != 0:
        # Increment the counter if the digit is odd
        odd_count += 1
    
    # Remove the last digit from the number
    number //= 10     #number = number // 10

# Print the original number and the count of odd digits
print(temp_number, "contains", odd_count, "odd digits")
