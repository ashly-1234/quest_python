# 2. Accept a string of space separated numbers and store them as a matrix (list of lists) of n rows. Now print the matrix row-wise

def create_matrix(data, n):
    numbers = list(map(int, data.split()))
    total_numbers = len(numbers)
    rows = n
    cols = total_numbers // n

    # Check if the numbers can be evenly divided into the specified number of rows
    if total_numbers % n != 0:
        print("Error: The total number of elements is not divisible by the number of rows.")
        return None

    # Create the matrix
    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(numbers[index])
            index += 1
        matrix.append(row)
    
    return matrix

# Read user input
data = input("Enter space-separated numbers: ")
n = int(input("Enter the number of rows: "))

matrix = create_matrix(data, n)

# Print the matrix row-wise if it was successfully created
if matrix:
    print("Matrix:")
    for row in matrix:
        print(row)
