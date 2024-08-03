#var arg function:
# A function that can take any number of arguments, from 0 to many.

def varArgFunction1(*arguments):
    print(arguments)
    print(type(arguments)) # tuple
 
def varArgFunction2(*arguments):
    for i in range(len(arguments)):
        print(arguments[i])           
 
varArgFunction1(1, 2, 4) #calling ftn one by one
varArgFunction1()
varArgFunction1('list', 'tuple', 'set', 'dictionary')
 
varArgFunction2(1, 2, 4)
varArgFunction2()
varArgFunction2('list', 'tuple', 'set', 'dictionary')
varArgFunction2('list', 'tuple', 'set', 'dictionary', 1)

def varArgFunction3(*arguments):
    print(arguments)
    # arguments[1] = 22                                 # TypeError. since tuple cannot add or remove values, ie, it is immutable
    arguments[5][0] = 20 # even though the list is inside the tuple, we can modify it.  here 5 is the index of list inside tuple . and 20 is added to 0th index of list not a tuple
    print(arguments)
    arguments[5].append(50)                              #add values at the end of the list inside
    print(arguments)
 
varArgFunction3(1, 2, 4, 'list', 4.5, [2, 3, 5])
 

 
''''
def varArgFunction2(*arguments):
        print(arguments)
 
def varArgFunction2(*arguments):
    for i in range(len(arguments)): #Loop with range() function
        print(arguments[i])
 
def varArgFunction2(*arguments):
    for element in arguments: # for each loop. It accesses all elements of the tuple one by one
        print(element)


'''
'''
 It is this concept or tool of Python using which the Function overloading concept is implemented alternatively. Thus, there is no need to Overload functions/methods in Python.
'''
 
