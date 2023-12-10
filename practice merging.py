# Casey: this is my experimentation with merging the Water Calculator class with our tkinter code
from tkinter import *
from tkinter import simpledialog
import tkinter as tk

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
            raise ValueError("Invalid value for 'activity_level'. Please use values 1-5.")
        return self.TDEE

    def final_intake(self):
        """Calculate and print the final water intake."""
        water_intake_oz = self.TDEE * 0.5
        water_intake_cups = water_intake_oz * 0.125
        print(f"Your daily water goal is {water_intake_oz:.2f} ounces, or {water_intake_cups:.2f} cups!")

class Frame1(tk.Frame):

    ''' Homepage'''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.load_images()

    # QUESTION FOR TA: should this method be moved into MainPage since Homepage should take you to InfoPage first and not Water_Calculator_Screen?
    def button(self):

        button = tk.Button(self, command = lambda: controller.show_frame(Water_Calculator_Screen))

        button.grid(row = 1, column = 0, pady = 10, padx = 10)

    # QUESTION FOR TA: is this okay how it is or is there a way to make it case specific for each frame?
    def load_image(self):

        image_path = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/MainPage().png"

        self.image = PhotoImage(file = image_path)


class InfoPage(Frame1):
    '''Info Page (Enter your information below). '''
    # QUESTION FOR TA:!!!!!! we need to add more for this one than others because it takes user input so likely needs more than just a button

    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        Water_Calculator().get_user_input()


calculator = Water_Calculator()
calculator.calc_BMR()
calculator.adjust_for_activity_level()
calculator.final_intake()