# Remove the negative numbers from a list of N numbers
def remove_negative_numbers(numbers):
    # Use a while loop with an index to remove negative numbers
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)  # Remove the element at index i
        else:
            i += 1  # Only increment index if no element is removed
    
    return numbers

# Accept the number of numbers from the user
N = int(input("Enter the number of numbers: "))

# Initialize an empty list to store the numbers
numbers = []

# Use a loop to accept N numbers from the user
for i in range(N):
    num = int(input(f"Enter number {i}: "))            
    numbers.append(num)

# Remove negative numbers
filtered_numbers = remove_negative_numbers(numbers)

# Print the result
print("List after removing negative numbers:", filtered_numbers)





'''
step1
function is defined to remove negative numbers - when the number < 0, the value is removed 

step2
number of elements to be entered is given

step3
empty list created

step5
append values in it

step6
function called

step7
print the list
'''