'''
Write a code to demonstrate use of inheritance and polymorphism using below example:
1. Eatable
1.1 Vegetarian
1.2 Non-Vegetarian

properties to be used: carbs, fat, protein, isPeelable, isBoneless

Place appropriate properties in parent class or child class and assign the values in __init__ 



'''
class Eatable:
    def __init__(self, carbs, fat, protein):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein

        print(f"food is of carbs: {carbs}, fat: {fat}, protein: {protein}")

class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, is_peelable):
        super().__init__(carbs, fat, protein)
        self.is_peelable = is_peelable

        if self.is_peelable == True:
            print('peelable')
        else:
            print("not peelable")    



class Non_Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, is_boneless):
        super().__init__(carbs, fat, protein)
        self.is_boneless = is_boneless

        if self.is_boneless == False:
            print('not boneless')
        else:
            print("boneless")
    


veg = Vegetarian(10, 2, 5, True)
non_veg = Non_Vegetarian(20, 10, 15, False)



    

 