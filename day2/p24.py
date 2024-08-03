# 9. Print a hollow square of n lines
# Input the number of lines for the square
n = int(input("Enter the number of lines for the hollow square: "))

# Iterate through each line
for i in range(n):
    # Print the square's borders or hollow spaces
    for j in range(n):
        # Check if it's the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    # Move to the next line
    print()

      
