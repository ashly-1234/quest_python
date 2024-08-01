#find sum of the series: n - n(2)/3 + n(4)/5 - n(8)/7 + ....upto m terms and (1<=n<=5) and (2<m<10)

def calculate_series(term_base_value, number_of_terms):
    # Initialize the sum with the first term
    total_sum = 0
    
    # Iterate through the terms
    for i in range(number_of_terms):
        # Compute the numerator and denominator for the current term
        numerator = number_of_terms * (2 ** i)
        denominator = 2 * i + 1
        
        # Calculate the current term with alternating signs
        term = (-1) ** i * numerator / denominator
        
        # Add the current term to the total sum
        total_sum += term
    
    return total_sum


term_base_value = int(input('Enter base value of every term (>= 1 and <= 5): '))  # within the range 1 to 5
number_of_terms = int(input('Enter number of terms of the series (>= 2 and < 10): '))  #  within the range 2 < m < 10
result = calculate_series(term_base_value, number_of_terms)
print(f"The sum of the series for term_base_value={term_base_value} and number_of_terms={number_of_terms} is: {result:.2f}")



 
# def findSumOfTerms(n, m):
#     sum_of_terms = 0
#     for i in range(1, m+1):
#         numerator = n ** 2 ** i
#         denominator = (2*i-1)
#         term = (numerator/denominator) * ((-1) ** (i-1))
#         sum_of_terms += term
 
 
# number_of_terms = int(input('Enter number of terms of the series (>= 2 and < 10): '))
 
# term_base_value = int(input('Enter base value of every term (>= 1 and <= 5): '))
 
# sum_of_terms = findSumOfTerms(term_base_value, number_of_terms)
 
# print(f'Sum of the terms is {sum_of_terms}')