# use of function, class, inheritance

# Inputs 
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter occupation: \nS. Student\nW. Working\nEnter any number.")
armed_force = input("In armed forces or parents in armed forces: \nY. yes\nN. no\nEnter any number.")
residence = input("Enter residence: \nH. Hosteller \nL. Localite\nEnter any number.")
residence_pin = int(input('Please enter your residence pin:'))
hostel_name = input('Please enter your hostel name:')

class Customer:
    discount_pin = [100001, 100002, 100003]
    hostels = ['abc', 'bcd', 'cde']

    def __init__(self, age, gender, occupation, armed_force, residence, residence_pin, hostel_name):
        self.age = age
        self.gender = gender.lower()
        self.occupation = occupation.lower()
        self.armed_force = armed_force.lower()
        self.residence = residence.lower()
        self.residence_pin = residence_pin
        self.hostel_name = hostel_name.lower()

    def senior_discount(self):
        if (self.age >= 60 and self.gender == "m") or (self.age >= 45 and self.gender == "f"):              #return true so that needn't repeat the same steps
            print("Senior citizen 15 percent discount applied, thank you for shopping")              
        
            

    def gender_discount(self):
        if self.age < 45 and self.gender == "f":
            print("100 rupees coupon on Nykaa, Fastrack, thank you for shopping")
        elif self.age < 60 and self.gender == "m":
            print("100 rupees coupon on Titan, Fastrack, thank you for shopping")
        else:
            print("No discount coupon, thank you for shopping")

    def armed_force_benefit(self):
        if self.armed_force == 'y':
            print("Free pass for Republic Parade, thank you for shopping")
        else:
            print("No free pass, thank you for shopping")

    def student_discount(self):
        if self.occupation == 's' and (self.gender == "f" or self.gender == "m") and self.age < 45:
            print("500 rupees coupon for books, thank you for shopping")
            self.hostel_discount()
        else:
            print("Thank you for shopping")

    def hostel_discount(self):
        if self.residence == 'h' and self.residence_pin in Customer.discount_pin and self.hostel_name in Customer.hostels:
            print("Groceries discount, thank you for shopping")
        else:
            print("No Groceries discount, thank you for shopping")

class Discounts(Customer):
    def shop(self):
        self.senior_discount()
        self.gender_discount()
        self.armed_force_benefit()
        self.student_discount()

customer = Discounts(age, gender, occupation, armed_force, residence, residence_pin, hostel_name)

customer.shop()
