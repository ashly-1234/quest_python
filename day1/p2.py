#check if user given input as a digit or not
print('Enter a character to check if it is a digit')
ch = input()

# if ch >= 48 and ch <= 57:            #We cannot use strings as integers in Python. If we try to do so, we get "TypeError" which is runtime error

# ValueError: If we try to convert a data into another type which is not possible. Example, trying to convert 'abc' into int()
#          
#  #The unicode/ascii values of the digits which are stored as characters in memory have their values starting from 48 to 57. That is the character '0' has value 48, '1' has 49 and '2' has 50 and so on upto '9' with value 57.


if ch >= '0' and ch <= '9':            #here using logical and. also we using the closed interval operator
    print('given character is a digit')
else:
    print('given character is Not a digit')