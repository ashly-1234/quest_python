# 6. Print the Pascals triangle of n lines


from math import factorial

lines = int(input("Enter the number of lines for Pascal Triangle: "))
for i in range(lines):
    for j in range(lines-i+1):
        print(end=" ")

    for j in range(i+1):
        # nCr = n!/((n-r)!*r!) => oCo 1Co 1C1 2C0 2C1 2C2 ...... 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    print()


    '''
    # Input the number of lines
n = int(input("Enter the number of lines for Pascal's Triangle: "))

for line in range(n):
    # Every line starts with 1
    number = 1
    # Print leading spaces for formatting
    print(' ' * (n - line), end='')
    for i in range(line + 1):
        # Print the current number and a space
        print(number, end=' ')
        # Update number to the next number in the row
        number = number * (line - i) // (i + 1)
    # Move to the next line
    print()

    
    '''