# check if the user given number idperfect square
import math
input_number = int(input("enter a number to check it is a perfect square"))
root_number = int(math.sqrt(input_number))
root_number_square = root_number * root_number
if root_number_square == input_number:
    print(f'{input_number} is a prefect square')
else:
    print(f'{input_number} is not a prefect square')