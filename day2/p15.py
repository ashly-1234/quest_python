# Program to find sum of digits in of number

input_number = int(input('Enter a number to find sum of digits in it: '))

sum_of_digits = 0
temp_number = input_number

while temp_number != 0:
    remainder_digit = temp_number % 10
    temp_number = temp_number // 10
    sum_of_digits += remainder_digit

print(f'Sum of digits in {input_number} is {sum_of_digits}')

# Alternate solution:

# input_number = int(input('Enter a number to find sum of digits in it: ')) # read a number and store it as an integer

# numbers = [int(char) for char in str(input_number)] # convert the number into string and read character by character from the string using for loop and then convert each of the character to integer and store it in the list.

# print(numbers) # Print the list of numbers

# print(f'Sum of digits of {input_number} is {sum(numbers)}') # The sum() finds sum of the elements of the list