# 3. Accept N strings and count the number of Palindromes in it.


def palindromes(strings):  # function to check palindrome or not 
    count = 0
    for string in strings:
        if string[::-1] == string:  #reverse each string and check if equal
            count += 1
    print("Number of palindrome string is:",count)

input_string = [string for string in input("Enter the strings to check Palindrome or not : ").split(' ')]

palindromes(input_string)