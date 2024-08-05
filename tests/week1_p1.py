
#Ashly		- 6 - Tsubasa and his Fest (2 sheets)




print("Enter the  number of testcases: ")
test_case_number = int(input())
for i in range(test_case_number):
    print("Enter the number of passes and id of first person:")
    number_of_passes,id1 = input().split()
    
    for j in range(int(number_of_passes)):
        print("Enter the string for pass or black values and their id:")
        string = input()
        if string[0]=='P':

            pass_black_value, id1 = string.split()
            list.append(int(id1))
        else:
            list.append(list[-2])

    print("Player" + str(list.pop()))

'''
step 1 
input the number  of passes 

step2 
iterate till we get the number of passes 

step3
create an empty list

step4
append those player's id who got pass as the current possessor


'''