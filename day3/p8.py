squares = []                               
for i in range(10):
	squares.append(i * i)                               #appending values
print('Squares = ', squares)

squares2 = [x**2 for x in range(10)]                    #list comprehension
print('Squares2 = ', squares2)

squares3 = list(map(lambda x: x**2, range(10)))          #range is used to generate values, lambda takes an argument x (one by one values), map ftn collect these values, map gives that collected values to list
print('Squares3 = ', squares3)





