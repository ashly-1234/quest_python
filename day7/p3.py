age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter occupation: \nS. Student\nW. Working\nEnter any number.")

if gender.lower() == "m":
    if age >= 60: 
        print("Senior citizen discount applied, thank you for shopping")
    else:    
        print("You get a voucher, thank you for shopping")
elif gender.lower() == "f":
    if age >= 45:
        print("Senior citizen discount applied, thank you for shopping")
    else:    
        print("You get a voucher, thank you for shopping")
elif occupation.lower() == "s":
    if age >= 45:
        print("Senior citizen discount applied, thank you for shopping")
    else:    
        print("You get a voucher, thank you for shopping")


    print("Thank you for shopping")



