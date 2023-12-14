# Casey: this is my experimentation with merging the Water Calculator class with our tkinter code
import tkinter as tk
from tkinter import simpledialog

class  Water_Calculator:

    def __init__(self):
        """Initialize the Calculator class."""
        self.get_user_input()
        self.bmr = None
        self.TDEE = None

    '''def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = int(input("Enter your age: "))
        self.sex = input("Enter your sex (m/f): ").lower()
        self.weight = float(input("Enter your weight in pounds: "))
        self.height = float(input("Enter your height in inches: "))
        self.activity_level = int(input("Enter your activity level from 1-5: "))'''

    # Casey: this is my experimentation with merging the Water Calculator class with our tkinter code
    def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = simpledialog.askinteger("Input", "Enter your age: ")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f): ").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds: ")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches: ")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5: ")

    def calc_BMR(self):
        """Calculate BMR based on the Harris-Benedict equation."""
        if self.sex == "m":
            self.bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif self.sex == "f":
            self.bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'm' or 'f'.")
        return self.bmr

    def adjust_for_activity_level(self):
        """Adjust BMR based on the user's activity level."""
        activity_multipliers = {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }

        if self.activity_level in activity_multipliers:
            self.TDEE = self.bmr * activity_multipliers[self.activity_level]
        else:
<<<<<<< Updated upstream
            raise ValueError("Invalid value for 'activity_level'. Please use values 1-5.")
        return self.TDEE

    def final_intake(self):
        """Calculate and print the final water intake."""
        water_intake_oz = self.TDEE * 0.03
        water_intake_cups = water_intake_oz * 0.125
        print(f"Your daily water goal is {water_intake_oz:.2f} ounces, or {water_intake_cups:.2f} cups!")



calculator = Water_Calculator()
calculator.calc_BMR()
calculator.adjust_for_activity_level()
calculator.final_intake()

=======
            raise ValueError("Invalid value for 'activity_level'. Please use one of: 'sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'.")
    
    def final_intake(self, TDEE, weight):
     
# Recommended water intake as a range (in ounces per pound of body weight)
        lower_bound_ratio = 0.5
        upper_bound_ratio = 1.0

        # Calculate the recommended water intake range
        lower_bound = weight * lower_bound_ratio
        upper_bound = weight * upper_bound_ratio

        # Calculate the total water intake based on TDEE
        water_goal = (lower_bound + upper_bound) / 2.0

        print("Your daily water goal is {water_goal} ounces!")
        
>>>>>>> Stashed changes
       
        


