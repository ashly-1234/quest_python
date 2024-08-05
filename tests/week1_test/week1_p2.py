#Shreya and her mon went to shopping

def max_earnings(number_of_shoes, pair_of_shoes_carry, prices):


   
    negative_prices = [price for price in prices if price < 0]
    
    # Sort the negative prices to get the most negative values first
    negative_prices.sort()
    
     
    return sum(negative_prices)


number_of_shoes, pair_of_shoes_carry = map(int, input().split())
prices = list(map(int, input().split()))

earnings = max_earnings(number_of_shoes, pair_of_shoes_carry, prices)
print(earnings)