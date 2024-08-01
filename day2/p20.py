# 5. Print an equilateral triangle of n lines
n = int(input("Enter the number of lines for the equilateral triangle: "))  # Take input from the user

for i in range(n):                         #The outer for loop iterates from 0 to n-1, where i represents the current row index.
    # Print spaces before the stars
    print(' ' * (n - i - 1), end='')       #The number of spaces before the stars decreases as the row index increases. For each row, it prints n - i - 1 spaces.
    # Print stars
    print('*' * (2 * i + 1))               #The number of stars increases as the row index increases. For each row, it prints 2 * i + 1 stars.

'''
Alternative
n = int(input("Enter the number of lines for the equilateral triangle: "))  # Take input from the user

for i in range(1, n + 1):
    # Print spaces before the stars
    print(' ' * (n - i), end='')
    # Print stars
    print('*' * (2 * i - 1))

'''