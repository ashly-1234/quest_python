# 7. Print the Fibonacci series of n terms with 1st 2 terms as 1 and 2.
n = int(input("Enter the number of terms for the Fibonacci series: "))  # Take input from the user

# Check if the number of terms is valid
if n <= 0:
    print("Number of terms must be positive.")
elif n == 1:
    print("1")
elif n == 2:
    print("1 2")
else:
    # Initialize the first two terms
    a, b = 1, 2
    print(a, b, end=' ')
    
    # Generate and print the rest of the series
    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=' ')
    print()  # New line at the end
