# 11.Print a hollow square of n line with the diagonals.
n = int(input("Enter the size of the square: "))  # Take input from the user

for i in range(n):
    for j in range(n):
        # Print '*' if it's on the border or diagonals
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or j == n - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # Move to the next line
