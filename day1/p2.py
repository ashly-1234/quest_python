#check if user given input as a digit or not
print('Enter a character to check if it is a digit')
ch = input()
if ch >= '0' and ch <= '9':            #here using logical and. also we using the closed interval operator
    print('given character is a digit')
else:
    print('given character is Not a digit')