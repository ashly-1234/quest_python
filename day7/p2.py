

input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")

try:
    num1 = int(input1)
    num2 = int(input2)
    print(num1 + num2)
except ValueError:
    try:
        print(input1 + " " + input2)
    except TypeError:
        print("A TypeError occur")








