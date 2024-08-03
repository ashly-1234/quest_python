# 4. Accept N strings, and check how many of them possess the string X

def check_substring(strings,sub):  # function to check how many of them possess the substring 
    count = 0
    for string in strings:
        if string.count(sub) == 1:  
            count += 1
    print("Number of substring is:",count)

input_string = [string for string in input("Enter the strings to check words possessing x : ").split(' ')]
substring = input("Enter the string to check: ")
check_substring(input_string,substring)



