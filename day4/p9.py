def varArgFunction(*arguments): # receives the data into a 'tuple'. However, if it has objects like list or dictionary, then they will received by reference only.
    print(arguments)
    arguments[0].remove(10)    # in the tuple , the list is stored at index 0 and from that list, 10 which we input is removed
 
def myFunction(user_given_list): # receives reference to the 'list' numbers2
    user_given_list.remove(35)
 
numbers1 = [int(num) for num in input().split(',')]      #actually what we write globally is the 'main ftn', but in python we just explicitly avoid writing main. here this is actually main ftn
#actually we entered list but in ftn it take as one of the arg of tuple

# input: 10,20,30,40,50

print(numbers1)
varArgFunction(numbers1)      # the list here is passed by reference
print(numbers1)
 
numbers2 = list(map(int, input().split()))         #input any values with spaces and with 35 in it bcz in ftn we remove it . we entered list. and it is list as well in ftn   
print(numbers2)
myFunction(numbers2)
print(numbers2)