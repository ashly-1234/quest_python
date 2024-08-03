numbers = [23, 7,19, 41, 29, 3, 47]
print('Numbers = ', numbers)
print('Max number = ', max(numbers))         #47
print('Min number = ', min(numbers))         #3
print('Number of elements = ', len(numbers)) #7
print('Sorted number = ', sorted(numbers))   #sort create copy of list, actual list is not modified
print('Numbers = ', numbers)
numbers.sort()                               #sort and modify original list
print('NUmbers = ', numbers)