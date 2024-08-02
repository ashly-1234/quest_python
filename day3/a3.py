# 3. Print the smallest and biggest sized strings from a list of N strings
def smallest_and_largest(strings):
    smallest = strings[0]                                    #smallest = largest = strings[0] initializes both smallest and largest to the first string in the list. This provides a starting point for comparisons.

    largest = strings[0]
    
    for string in strings[1:]:
        if len(string) < len(smallest):
            smallest = string
        if len(string) > len(largest):
            largest = string
    
    return smallest, largest

number_of_strings = int(input("Enter the number of strings: "))

strings = []
for _ in range(number_of_strings):
    string = input("Enter string: ")
    strings.append(string)

smallest, largest = smallest_and_largest(strings)                  #ftn call


if smallest is not None and largest is not None:
    print(f"The smallest string is: {smallest}")
    print(f"The largest string is: {largest}")
else:
    print("The list of strings is empty.")

    
'''
step 1
function to find smallest and largest string is defined

step2
prompt user to enter number of strings

step3
append strings in the empty list that was created

step4
call the function

step5
print if strings found

'''    