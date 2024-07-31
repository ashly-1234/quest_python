# Checking a number is Single Digit or not

Number = int(input("Enter the number which need to check if it is SIngle Digit or not : "))
if Number//10 == 0:
    print(Number," is Single Digit")
else:
    print(Number ," is not Single Digit")