#Global methods and keywords:

numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
print(numbers) # [1, 4, 5]    => list gets modified
del numbers[1]
print(numbers) # [1, 5]
del numbers[:] # we are deleting all the elements from the list
print(numbers) # []
numbers.insert(0,10) # inserting the element 10 at index 0?
print(numbers)   
 
#INSERT ELEMENT AT REAR OF THE LIST: 3 different ways
# a.insert(len(a), x)
# a.append(x)
# a.[len(a):] = [element]            #by list slicing to append
 
# Below is an error
# numbers[len(numbers):] = 3
# TypeError because we must assign only a list(iterable) not a primitive value


numbers = [1, 2,]
numbers.append (3) # slicing
print(numbers)
numbers[len(numbers):] =[3]   #alternate way of doing the append using list #extends
print(numbers)
numbers.insert(len(numbers), 5)  #insert  at end
print(numbers)
numbers.insert(-1, 9)   #insert at the 2nd last
print(numbers)
#numbers[len(numbers):] = 3  #TypeError: can only assign an iterable(list) not a primitive
names =['pune', 'panjim', 'purola']
names.insert(-1,'palakkad')           #insert at the 2nd last
print(names)
