#class practice 

class Person:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender

class Student(Person):           #student is child class of person as the parent class so needed all its parameter

    #function can have one __init__ block in python while other languages can have multiple __init__ block

    def __init__(self, age, gender, pincode, residence):
        super().__init__(self,age,gender)
        self.pincode = pincode
        self.residence = residence
    def __init__(self, age, gender, pincode, residence, isquota):
        super().__init__(self,age,gender)
        self.pincode = pincode
        self.residence = residence
        print("Sports quota")        

class Employee(Person):
    def __init__(self, age, gender, pincode):
        super().__init__(age, gender)  
        self.pincode = pincode     

# s1 = Student(20, "female", 100001, "hosteller")
s2 = Student(20, "female", 100001, "hosteller", "True")

# e1 = Employee(30, "female", 100002)
    
        


        