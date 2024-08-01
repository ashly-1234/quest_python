# 9. Print a hollow square of n lines
n = int(input("Enter the size of the square: "))  # Take input from the user

for i in range(n):
    if i == 0 or i == n - 1:
        # Print the first and last rows as solid lines
        print('*' * n)
    else:
        # Print the hollow rows
        print('*' + ' ' * (n - 2) + '*')
