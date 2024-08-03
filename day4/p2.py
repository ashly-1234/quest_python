# List Slicing:
 
numbers = [2, 9, 7, 5, 3, 13, 19, 17, 29]

print(numbers)              # we get the complete list
print(numbers[0])           # we get the 1st element
print(numbers[-1])          # we get the last element. Hence, we see that -ve indexing is possible in Python
print(numbers[-2])          # we get 2nd  last  element from the list
print(numbers[:])           # we get the complete list. Here, we have written nothing before the colon and hence it is treated as 0, which means start from the beginning of the list. Here also have not written anything after the colon, which means it is treated as UP TO END OF THE LIST. 

print(numbers[:3])          # Start from index 0 and access elements up to index 3-1 which is 2.
print(numbers[1:-1])        # Start from index 1 (2nd element) and access elements up to last but not print the last element, because -1 is the index of last element and we must not include it.

print(numbers[1:8:2])       # start from index 1 and access upto index 8-1 and increment each time by 2 elements. So o/p is [9, 5, 13, 17]
print(numbers[::3])         # start from beginning and go up to end of the list with increment of 3 in position(skip 2 elements) and print
print(numbers[8:1:-2])      #Start from index 8, go up to index 2(as 1 - (-1)) with decrement of 2 (or increment of -2)

print(numbers[::-1])        # Since the increment is negative, we understand that we have to move in reverse (meaning from the end to towards the start). The area within the list we have to access is all the elements, because nothing is specified before and after the 1st colon :

print(numbers[1:20])        #we will get complete list even though we don't have element till 20th index

#           #                    #                #

print(numbers[1:8:-2])      #here we get an empty list as here we require increment value not the decrement value
print(numbers[20:1])        #we get empty list as we don't mention any increment or decrement
print(numbers[20:1:1])      #here we get empty list since we have to give decrement value
print(numbers[20:1:-1])     #here we can reverse the list

print(numbers[:1:])         #here we get value of 0th index ie, end value will be always end value -1 => (1-1 = 0)
print(numbers[8:0:-2])      #start from 8th index till index 1


numbers1 = [1, 2, 3]
print(numbers1[:1:-2])       # treated as: print(numbers[-1:1:-2])So, start from last possible index, go upto index 1, with decrement of 2 ---------whenever we mentioned increment as negative also we did not mention where to start with, then python always consider the start as last element and hence we get the answer as 3 

