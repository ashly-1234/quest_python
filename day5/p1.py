# Program to create 1D Array (List) and find biggest and smallest numbers in it.
 
n = int(input('Enter size of the Array: '))
 
array = []
print(f'Enter {n} numbers of the Array')
for i in range(n):
    array.append(int(input()))
   # array.insert(0, int(input()))    cannot use insert as it append the value at the starting
 
print('Array = ', array)
small_num = array[0]
big_num = array[0]
 
for i in range(1, n):        #here we start with 2nd value ie, index=1 , since we already assigned the value in index 0 to small and big number to do the comparision      
    #here we used this method so that we strictly needed to go till  n numbers to find the biggest and smallest
    if array[i] < small_num:
        small_num = array[i]
    if array[i] > big_num:
        big_num = array[i]
print(f'Biggest number in Array is {big_num}')
print(f'Smallest number in Array is {small_num}')