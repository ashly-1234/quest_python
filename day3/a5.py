# Demonstrate the different ways of adding elements to a list and different ways to delete elements from a list.

# adding elements to a list

# append() method      -Adds a single element to the end of the list
list1 = [1, 2, 3, 4, 5]
list1.append(6)
print("List after append:", list1)

# insert() method      -Inserts an element at a specified index in the list
list2 = [1, 2, 3, 4, 5]
list2.insert(4, 'a')
print("List after insert:", list2)

# extend() method   - add many elements at the end

list3 = [1, 2, 3, 4, 5]
list3.extend([7, 8])
print("List after extend:", list3)

#List Concatenation - + Operator  - Concatenates another list to the existing list.
list4 = [1, 2, 3]
list4 = list4 + [4, 5]
print("After concatenation:", list4)

my_list1 = [1, 2, 3, 4, 6]
my_list1 = my_list1 + ['a', 'b']
print("After concatenation:", my_list1)  


# list Comprehension  - Creates a new list by applying an expression to an existing iterable
my_list2 = [1, 2, 3]
doubled_list = [x * 2 for x in my_list2]  # Double each element
print("After list comprehension:", doubled_list)  

# Deleting Elements from a List:

# remove()   -Removes the first occurrence of a specified value
list6 = [1, 2, 3, 2, 4]
list6.remove(2)
print("After remove:", list6)

# pop() -Removes and returns the element at the specified index. If no index is provided, removes and returns the last element.
list7 = [1, 2, 3, 4]
element = list7.pop(3)
print("After pop:", list7) 
print("Popped element:", element)

# del  -Deletes an element at a specified index or the entire list
list8 = [1, 2, 3, 4]
del list8[2]
print("After del:", list8)

# clear   -Removes all elements from the list, leaving it empty.
list9 = [1, 2, 3, 4]
list9.clear()
print("After clear:", list9)

#Using List Slicing -Removes a range of elements by slicing.

my_list3 = [1, 2, 3, 4, 5]
my_list3[1:3] = []  # Removes elements at indices 1 and 2
print("After slicing:", my_list3)  

#Using List Comprehension -Creates a new list excluding certain elements
my_list4 = [1, 2, 3, 4, 5]
filtered_list = [x for x in my_list4 if x % 2 == 0]  # Keep only even numbers
print("After list comprehension (filtering):", filtered_list)  

