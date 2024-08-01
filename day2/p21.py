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