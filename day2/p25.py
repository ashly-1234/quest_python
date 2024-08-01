# 10.Print X shape made up of stars of n lines
n = int(input("Enter the number of lines for the X shape: "))  # Take input from the user

for i in range(n):                      #Iterate over each row from 0 to n-1
    for j in range(n):                  #Iterate over each column from 0 to n-1

        if j == i or j == n - i - 1:    #Print * when the column index j is equal to the row index i (diagonal from top-left to bottom-right).
                                        #Print * when the column index j is equal to n - i - 1 (diagonal from top-right to bottom-left).
            print('*', end='')
        else:
            print(' ', end='')          #Print a space for all other positions.
    print()  # Move to the next line
