
#Program to check if a number is Prime
import math
 
input_number = int(input('Enter a number to check if it is Prime: '))
 
prime = True # Assume the number is Prime
for i in range(2, math.ceil(math.sqrt(input_number)+1)):
    if input_number % i == 0: # if N is divisible by any number other than 2 and itself
        prime = False
        break # break the loop
if prime:
    print(f'{input_number} is Prime number')
else:
    print(f'{input_number} is not a Prime number')
 













'''
Read N
prime = true # assume the number N is Prime
for i from 2 to ciel(sqrt(N)) do:
	if N % i is 0 then:
		print N is not Prime number
		prime = false
		break the loop
if prime then:
	print N is a Prime number
'''
