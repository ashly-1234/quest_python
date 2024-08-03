# Program to create 2D Array, that is, a Matrix(using List) and add it to another Matrix and print the sum Matrix.
 
rows = int(input('Enter number of rows of the Matrix: '))
columns = int(input('Enter number of columns of the Matrix: '))
 
matrix1 = []
for i in range(rows):
    print(f'Enter {columns} numbers of Row-{i+1}')  # i + 1 is to print the row number as 1 , 2 , 3 ...
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)
 
for row in matrix1:
   # print(row)            #prints as list in 2D

    for number in row:     #to create as matrix

        #print('%-3s'%(number), end='')   - for left align -ve

        print('%3s'%(number), end='')   #   for right align  +ve    , end='' means to be in same line

    print()                #move to nxt line