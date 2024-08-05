# PDB (Python Debugger)
 
# python -m pdb <name>.py[args] 		(begin the debugger)
 
# help[command] view a list of commands, or view help for a specific
# command
 
# within a python file:
# import pdb
# ...
# pdb.set_trace() 
# Add the above call to begin the debugger at this line when the file is run normally.
 
# NAVIGATING CODE: (within the Pdb interpreter)
# l(ist) 		list 11 lines surrounding the current line
# w(here) 	display the file and line number of the current line
# n(ext) 		execute the current line
# s(tep) 		step into function called at the current line
# r(eturn) 	execute until the current function’s return is
# encountered
 
# CONTROLLING EXECUTION:
# b[#] 		create a breakpoint at line [#]
# b 			list breakpoints and their indices
# c(ontinue)	execute until a breakpoint is encountered
# clear[#] 	clear breakpoint of index [#]
 
# CHANGING VARIABLES / INTERACTING WITH CODE:
# p<name> 	print value of the variable <name>
# !<expr> 	execute the expression <expr>
# NOTE: this acts just like a python interpreter
# run[args] 	restart the debugger with sys.argv arguments [args]
# q(uit) exit the debugger

#program to find nth fibo term
import math
term_number = int(input ("Enter N to print the Nth Fibo term: "))  
 
def find_nth_fibo_term(n):
    thrid_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:
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
 
if term_number <= 0:  
    print ("Please enter a positive integer, the given number is not valid")
else:
    print (f'The {term_number}th Fibo number is ', find_nth_fibo_term(term_number))


 
def check_if_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
 
input_number = int(input('Enter the number N, to print Nth Prime number: '))
 
j = 0
if input_number == 1:
    j = 2
elif input_number == 2:
    j = 3
else:
    count = 2
    j = 4 #Number in J is checked if Prime or not
    while count <= input_number:
        if check_if_prime(j):
            count += 1
            if count == input_number:
              break
        j += 1
print(f'{input_number}th Prime number is {j}')
