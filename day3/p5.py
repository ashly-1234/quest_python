#Find sum of the series: 1 - n + n(2) - n(3) + ..... m terms
 
                                                 #n(2) => n^2 ?   also here no indexing only position from 1 to ...


N = int(input('Enter the value of term:'))
M = int(input('Enter the number of terms:'))
sum_of_terms = 0
 
for i in range(0,M):
    term = ( N ** i) * ((-1) ** i)
    sum_of_terms += term
 
print('sum of the series is '+ str(sum_of_terms))



'''
def sum_series(base_number_n, term_number_m):
    sum = 0
    for i in range(term_number_m):
        sum += ((-1) ** i) * (base_number_n ** i)
    return sum


base_number_n = int(input("Enter base number"))        # base number
term_number_m = int(input("Enter number of terms"))    # number of terms
result = sum_series(base_number_n, term_number_m)
print(f"The sum of the series for base_number_n={base_number_n} and term_number_m={term_number_m} terms is: {result}")
'''


        
