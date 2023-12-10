import sys

class  Water_Calculator:
     
    def __init__(self, age, sex, weight, height, activity_level):
        """Initialize the Calculator class.
        list of attributes
        """
        self.age = age
        self.sex = sex 
        self.weight = weight
        self.height = height
        self.activity_level = activity_level 


    def calc_BMR(self):
        """BMR is aBasal Metabolic Rate based off of the Harris-Benedict equation """
       
        if self.sex == "m":
            bmr = 66 + (6.23(self.weight)) + (12.7(self.height)) - (6.8(self.age))   
        elif self.sex == "f":
            bmr = 655 + (4.35(self.weight)) + (4.7(self.height)) - (4.7(self.age))
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'M' for male or 'F' for female.")
        
        return bmr
        

    
    def adjust_for_activity_level(self, bmr):
        # adjust BMR based off of how active you are
        activity_multipliers = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
        }

        if self.activity_level in activity_multipliers:
           tdee = bmr * activity_multipliers[self.activity_level] # TDEE is total daily energy expenditure
        else:
            raise ValueError("Invalid value for 'activity_level'. Please rate your activity level on a scale from 1-5.")
        
        return tdee
    
    def final_intake(self, tdee):
        water_intake_oz = tdee(0.5)
        water_intake_cups = water_intake_oz(0.125)
        return (f"Your daily water goal is {water_intake_oz} ounces, or {water_intake_cups} cups!")
    