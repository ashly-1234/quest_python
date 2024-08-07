 
#male not senior: 100 voucher fastrack
#female : nyka
#occupation: student, working
#hostellor: 250 on groceries, localite
# if any of parent in armed forces/police
#Pass to R-Day parade

# * Name
# * Age
# 15% discount for all product for senior citizen
# * Gender
# male senior citizen (60 and above)
# female senior citizen (45 and above)
# 100 rupees nyka, fastrack, if female (<45)
# 100 coupon on titan, fastrack, if male (<60)

# ----
 
# *Occupation: Working, Student (PIN code should be local)
# College: 500 coupon on books
# Working: NA
 
# ----

# *Residence: Hosteller, Localite (Hostel name should be valid)
# Hosteller: Groceries
# Localite: NA
 
# ----

# * Armed Forces: Yes/No (Check from external file)
# Yes: Free pass for R-day parade for 2
# No: Na
 
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter occupation: \nS. Student\nW. Working\nEnter any number.")
armed_force = input("In armed forces or parents in armed force: \nY. yes\n N. no\nEnter any number.")
residence = input("Enter residence: \nH. hosteller \nL.localite\nEnter any number.")
 

if (age >= 60 and gender.lower() == "m") or (age >= 45 and gender.lower() == "f"):
    print("Senior citizen 15 percent discount applied, thank you for shopping")
else:    
    if age < 45 and gender.lower() == "f":
        print("100 rupees coupon on nyka, fastrack, thank you for shopping")  
    elif age < 60 and gender.lower() == "m":
        print("100 coupon on titan, fastrack, thank you for shopping")
    else: 
        print("No discount, thank you for shopping")

if occupation.lower() == 's' and age <= 45:
    print("500 coupon for books, thank you for shopping")
    if residence.lower() == 'h':
        print("Groceries discount, thank you for shopping")
    else:
        print("No discount, thank you for shopping")    

    if armed_force.lower() == 'y':
        print("Free pass for republic parade, thank you for shopping")
    else:
        print("No free pass, thank you for shopping")
        
else:
    print("thank you for shopping")































# ---------------------------------------------------------------------------------------------
# if age >= 60 and gender.lower() == "m":
#     print("Senior citizen 15 percent discount applied, thank you for shopping")
#     if occupation.lower() == "w" and armed_force.lower() == 'y':
#          print("Free pass for Republic day parade, thank you for shopping")
#     else:
#         print("Not applicable,thank you for shopping")
# elif age < 60 and gender.lower() == "m":
#         print("100 coupon on titan, fastrack, thank you for shopping")
#         if armed_force.lower() == 'y':   
#             print("Free pass to republic parade, thank you for shopping")
#         else:
#             print("Free pass to republic parade not applicable, thank you for shopping")
# elif age < 60 and gender.lower() == "m" and occupation.lower() == "w":
#     if armed_force.lower() == 'y':   
#         print("Free pass to republic parade, thank you for shopping")
#     else:
#         print("Free pass to republic parade not applicable, thank you for shopping")
# elif age < 60 and gender.lower() == "m" and occupation.lower() == "s": 
#     print("500 coupon for books, thank you for shopping")
#     if residence.lower() == 'h':           
#         print("Groceries discount, thank you for shopping")
#     else:
#         print("Not applicable, thank you for shopping")  
# elif age < 60 and gender.lower() == "m" and occupation.lower() == "s" and armed_force.lower() == 'y': 
#     print("Free pass to republic parade, thank you for shopping")
# elif age < 60 and gender.lower() == "m" and occupation.lower() == "s" and armed_force.lower() == 'n': 
#     print("Not applicable, thank you for shopping")    
            

# elif age >= 45 and gender.lower() == "f":
#     print("Senior citizen 15 percent discount applied, thank you for shopping")
#     if occupation.lower() == "w" and armed_force.lower() == 'y':
#          print("Free pass for Republic day parade, thank you for shopping")
#     else:
#         print("Not applicable,thank you for shopping")
# elif age < 45 and gender.lower() == "f":
#         print("100 rupees coupon on nyka, fastrack, thank you for shopping")
#         if armed_force.lower() == 'y':   
#             print("Free pass to republic parade, thank you for shopping")
#         else:
#             print("Free pass to republic parade not applicable, thank you for shopping")
# elif age < 45 and gender.lower() == "f" and occupation.lower() == "s":
#     if armed_force.lower() == 'y':   
#         print("Free pass to republic parade, thank you for shopping")
#     else:
#         print("Free pass to republic parade not applicable, thank you for shopping")
# elif age < 45 and gender.lower() == "f" and occupation.lower() == "s": 
#     print("500 coupon for books, thank you for shopping")
#     if residence.lower() == 'h':           
#         print("Groceries discount, thank you for shopping")
#     else:
#         print("Not applicable, thank you for shopping")  
# elif age < 45 and gender.lower() == "f" and occupation.lower() == "s" and armed_force.lower() == 'y': 
#     print("Free pass to republic parade, thank you for shopping")
# elif age < 45 and gender.lower() == "f" and occupation.lower() == "s" and armed_force.lower() == 'n': 
#     print("Not applicable, thank you for shopping")  

# else:
#     print("Thank you for shopping")                         
