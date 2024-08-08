'''
Coding tasks:
From the discussed program, do following:
1. Handle inputs with exception. String operation code is given below for your reference
2. Take only particular number of inputs: 1 for branch, 1 or more for pref and exact three for marks
3. Pseudo code is given below for your reference

Acceptance criteria:
Figure out 10 use cases and expected results in excel.
The program which you have made should run for 1 preference, that is, Accounts vacancy opening.

-------------
[ECE, Mech, BCOM]
[Maths, English, Art]

* Name
* Branch: ECE  					
* Preference: Maths, Art
--
* Maths: 80
* English: 96
* Art: 97

pass marks is 35

Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)

Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)

Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)

-------------  String operation code snippet ----------------
i = "MATHS, ART"
print(type(i))
listMarks = i.split(',')
print(type(listMarks))
print(len(listMarks))


-------------  logic ---------------------
# try:
#input branch: 1   #only 1
#input pref : 1,2,3  #1 or more
#input marks: 97,96,97   #exact 3
# except:
    #please provide valid inputs

#use dictionary to convert console number input to actual text

# occupation=='3'

# branch loop
    # pref loop
        #applicant should be pass in all subject
            # if #Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)
            # elif Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)
            # elif Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)
            # else : no openings for provided criteria


'''
branches = {1: "ECE", 2: "Mech", 3: "BCOM"}
preferences = ["Maths", "English", "Art"]

marks = {}
# subjects = ["Maths", "English", "Art"]

# Input for branch selection
branch_input = int(input("Enter the number for your branch (1, 2, 3): "))
branch = branches[branch_input]

# Input for preferences with validation
pref_input = input("Enter your preferences separated by commas: ")
pref_list = []
for pref in pref_input.split(","):
    pref = pref.strip().lower()
    pref_list.append(pref)

# Check if the number of preferences is more than 3
if len(pref_list) > 3:
    print("Error: You can only enter up to 3 preferences.")
    exit()

try:
    for preference in preferences:
        mark = input(f"Enter marks for {preference}: ")
        if mark == "":  # Handle blank input
            mark = "0"
        marks[preference.lower()] = int(mark)

    print("Marks scored by each subject:", marks)

except ValueError:
    print("Invalid input. Please enter a valid number for marks.")

try:
    # Check if passed in all subjects
    passed = True
    for mark in marks.values():
        if mark <= 35:
            passed = False
            break

    # Validate input criteria based on branch and preferences
    if branch == "ECE":
        if "art" in pref_list and "english" in pref_list:
            if ("art" in marks and marks["art"] > 90) and ("english" in marks and marks["english"] > 90) and passed:
                print("Eligible for Marketing vacancy opening.")
            else:
                print("Not eligible for Marketing vacancy opening.")
        else:
            print("Not eligible for Marketing vacancy opening.")
    elif branch == "Mech":
        if "maths" in pref_list and "english" in pref_list:
            if ("maths" in marks and marks["maths"] > 90) and ("english" in marks and marks["english"] > 90) and passed:
                print("Eligible for Sales vacancy opening.")
            else:
                print("Not eligible for Sales vacancy opening.")
        else:
            print("Not eligible for Sales vacancy opening.")
            
    elif branch == "BCOM":
        if "maths" in pref_list:
            if ("maths" in marks and marks["maths"] > 90) and passed:
                print("Eligible for Accounts vacancy opening.")
            else:
                print("Not eligible for Accounts vacancy opening.")
        else:
            print("Not eligible for Accounts vacancy opening.")
    else:
        print("Invalid branch selected.")

except ValueError:
    print("Invalid input.")
