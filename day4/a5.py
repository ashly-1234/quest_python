# 5. 

'''
Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.
 
main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
presence = [1, 0, 1, 0]
'''
def check_substrings(main_strings, sub_strings):
    results = []
    for i in range(len(main_strings)):
        if sub_strings[i] in main_strings[i]:
            results.append(1)
        else:
            results.append(0)
    return results

# Read user input for the number of strings
n = int(input("Enter the number of strings: "))

# Read the main strings
main_strings = [input(f"Enter main string {i + 1}: ") for i in range(n)]

# Read the substrings
sub_strings = [input(f"Enter substring {i + 1}: ") for i in range(n)]

# Check substrings and create the results list
results = check_substrings(main_strings, sub_strings)

# Print the results
print("Results:", results)

