
# Program to count the number of digits in a number
 
input_number = int(input('Enter a number to count number of digits in it: '))

count_of_digits = 0
temp_number = input_number

while temp_number != 0:
    temp_number = temp_number // 10
    count_of_digits += 1

print(f'Number of digits in {input_number} is {count_of_digits}')

'''
inp=3475
temp=3475
c=0

i=1
temp=347
c=1

i=2
temp=34
c=2

i=3
temp=3
c=3

i=4
temp=0
c=4

O/P: Number of digits in 3475 is 4

Alternate and easy solution:


input_number = int(input('Enter a number to count number of digits in it: '))

count_of_digits = len(str(input_number))

print(f'Number of digits in {input_number} is {count_of_digits}')
'''