
# Accept N numbers from the user and swap the consecutive elements in the list
def swap_elements(list):
    for i in range(0, len(list) - 1, 2):                #accesses every second element starting from the first element
        list[i], list[i + 1] = list[i + 1], list[i]
    return list

element_limit = int(input("Enter the number of elements: "))

list = []
for i in range(element_limit):
    element = int(input("Enter a number: "))
    list.append(element)

swapped_numbers = swap_elements(list)

print("List after swapping consecutive elements:", swapped_numbers)

'''
step 1
function is defined to swap consecutive element

step 2
prompt the user to enter the number of elements they want to input.

step 3
empty list created

step 4
add elements to the list using append method in a loop


step 5
call the function and print the result


'''
