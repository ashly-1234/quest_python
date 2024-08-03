# Find the nth term of the series 1 2 2 3 3 5 5 7 8 11 13 13


# here we have alternatively fibonacci series in odd positions and prime numbers in even positions
# here positions doesn't take the index as in the cases of list ie, starts with position 1,2.....N

#to get prime numbers, we take N//2 value as the count since they are in even position => O(n square ) as the time complexity, and for fibonacci series, we take N //2 + 1 term => o(n) as time complexity

import math

def nth_fibo_term(n):   # Function for get the last fibo term
    thrid_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:           # The first and second term of fibo series is 1 & 2 so we can    directly give the terms
        thrid_number = 1
    elif n == 2:
        thrid_number = 2
    else:
        thrid_number  = 0
        count = 2
        while count <= n:
            thrid_number = first_number + second_number
            count += 1
            if count == n:
                return thrid_number
            first_number = second_number
            second_number = thrid_number
    return thrid_number

##########################################################################################

def check_if_prime(num):           # Function to check if the given number is prime or not
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

###########################################################################################

def nth_prime(term_number):     # Function to get the last prime term
    j = 0
    if term_number == 1:
        j = 2
    elif term_number == 2:
        j = 3
    else:
        count = 2
        j = 4                   #Number in J is checked if Prime or not
        while count <= term_number:
            if check_if_prime(j):
                count += 1
            if count == term_number:
                break
            j += 1
    return j

##################################################################################


term_number = int(input ("Enter term number to be printed : ")) 

if term_number % 2  == 0:          # Checking which term it is, ie. is it fibo or prime
    terms = term_number // 2        # since prime series in even position 
    nth_prime_number = nth_prime(terms)
    print(term_number,"th term in the 1 2 2 3 3 5 5 7 8 ... is ", nth_prime_number)
else:
    terms = (term_number // 2) + 1   #fibo series in odd position
    nth_fibo_number = nth_fibo_term(terms)
    print(term_number,"th term in the 1 2 2 3 3 5 5 7 8 ... is ", nth_fibo_number )