# find smallest and biggest elements in a list of N numbers

# Accept the number of elements from the user
N = int(input("Enter the number of elements: "))

# Accept N numbers from the user in a single line, separated by spaces
numbers = list(map(int, input("Enter the numbers: ").split()))

# Find the smallest and biggest elements using min() and max() functions - built-in ftn 
smallest = min(numbers)
biggest = max(numbers)

# Print the smallest and biggest elements
print("Smallest element:", smallest)
print("Biggest element:", biggest)


'''
Algorithm
-------------------
step 1
Enter the number of elements

step 2
Prompts the user to enter the numbers, all in one line, separated by spaces.
Reads the input as a string.
Splits the input string into a list of substrings.
Converts each substring to an integer using map(int, ...).
Converts the map object to a list of integers and stores it in numbers.

step3
Find the smallest and biggest elements



step4
Print the smallest and biggest elements
'''