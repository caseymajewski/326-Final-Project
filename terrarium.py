# 326-Final-Project
from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.simpledialog import askfloat
from tkinter import Frame
from button import ImageButtonApp

#changed names
class  Water_Calculator():

    def __init__(self):
        """Initialize the Calculator class."""
        self.get_user_input()
        self.bmr = None
        self.TDEE = None

    def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = simpledialog.askinteger("Input", "Enter your age:")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):")
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")

    '''def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = simpledialog.askinteger("Input", "Enter your age: ")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f): ").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds: ")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches: ")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5: ")
    '''

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
        water_intake_goal_oz = self.TDEE * 0.03
        water_intake__goal_cups = water_intake_goal_oz * 0.125
        self.water_goal = water_intake_goal_oz
        message = f"Your daily water goal is {water_intake_goal_oz:.2f} ounces, or {water_intake__goal_cups:.2f} cups!"
        

        # Show the message in a popup
        messagebox.showinfo("Water Intake Result", message)
        return self.water_goal



class WaterTracker(Water_Calculator):
    def __init__(self):
        """Initialize the WaterTracker class.
         Args: 
         Percentage- defaults to None for now, represents the percentage of the user's water intake"""
        super().__init__()
        super().final_intake()
    def check_water_intake(self):
        self.user_water_intake = 0
        while self.user_water_intake < self.water_goal:
        # Ask the user how much water they have drunk today
            try:
                amount = float(input("How much water have you drunk today?: "))
                self.user_water_intake += amount
                # Compare the user's water intake with the target water intake
                percentage = round((self.user_water_intake / self.water_goal) * 100, -1)
                self.update_terrarium_water_level(amount, percentage)
                if percentage >= 100:
                    print("Congratulations! You have met your daily water goal.")
                else:
                    print(f"Keep Going! You only drank {percentage}% of your daily water goal.\nYou need to drink {self.water_goal - self.user_water_intake} more ounces of water to reach your goal")
            except ValueError:
                print("Invalid Input. Please enter a numeric value!")
        return percentage
        

    def update_terrarium_water_level(self, amount, percentage):
        """
        Update the water level in the terrarium.

        Parameters:
        amount (float): The amount of water to update the terrarium water level with.
        percentage (float): The percentage of the water goal achieved by the user.
        """
        frame_index = int(percentage / 10)  # Assuming 10% intervals
        benchmark_name = f"Benchmark{frame_index}"
        frame = self.get_benchmark_class(percentage)

        if frame:
            # Update the water level in the corresponding frame
            frame.update_water_level(amount)  # Pass the amount parameter to the method
        else:
            print(f"Unable to find the corresponding frame for percentage {percentage}%.")
        return benchmark_name

    def get_benchmark_class(self, benchmark_name):
        return globals().get(benchmark_name)


class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        '''container = Frame(self)
        container.grid(row=1, column=1)'''

        # Create an instance of WaterTracker with the calculated water goal
        self.water_tracker = WaterTracker()
        self.Water_Calculator= Water_Calculator

        # Create instances of frames and add them to the frames dictionary
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake(self):
            water_intake = self.water_tracker.check_water_intake()
            if 0 <= water_intake and water_intake <= 10:
                return Benchmark0
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 10.1 <= water_intake and water_intake <= 20:
                return Benchmark1
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 20.1 <= water_intake and water_intake <= 30:
                return Benchmark2
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 30.1 <= water_intake and water_intake <= 40:
                return Benchmark3
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 40.1 <= water_intake and water_intake <= 50:
                return Benchmark4
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 50.1 <= water_intake and water_intake <= 60:
                return Benchmark5
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 60.1 <= water_intake and water_intake <= 70:
                return Benchmark6
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 70.1 <= water_intake and water_intake <= 80:
                return Benchmark7
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 80.1 <= water_intake and water_intake <= 90:
                return Benchmark8
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 90.1 <= water_intake and water_intake <= 99:
                return Benchmark9
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
            water_intake = self.water_tracker.check_water_intake()
            if 100 <= water_intake and water_intake <= 110:
                return Benchmark10
        

            
class Benchmark(MainPage):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(self, parent, controller, water_tracker)
        self.parent = parent
        self.controller = controller
        self.water_tracker = water_tracker
    
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        
        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(user_water_intake)

        # Get the benchmark class based on the current percentage
        percentage = round((self.water_tracker.user_water_intake / self.water_tracker.water_goal) * 100, -1)
        benchmark_class = self.water_tracker.get_benchmark_class(percentage)

        # Transition to the corresponding benchmark
        if benchmark_class:
            self.controller.show_frame(benchmark_class.__name__)
        else:
            print(f"Unable to find the corresponding benchmark for percentage {percentage}%.")
        

        # Show the initial frame (change this to the desired initial frame)
        self.show_frame(Benchmark1)



class Benchmark0(Benchmark):
    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        
        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(user_water_intake)
       
class Benchmark1(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img)

class Benchmark2(Benchmark): 
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img2)

class Benchmark3(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img3)

class Benchmark4(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img4)

class Benchmark5(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img5)

class Benchmark6(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img6)

class Benchmark7(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img7)

class Benchmark8(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img8)

class Benchmark9(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img9)

class Benchmark10(Benchmark):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.image_app = ImageButtonApp(img10)

if __name__ == "__main__":
    main = MainPage()
    main.mainloop()

    img = '10%.png'
    img2 = '20%.png'
    img3 = '30%.png'
    img4 = '40%.png'
    img5 = '50%.png'
    img6 = '60%.png'
    img7 = '70%.png'
    img8 = '80%.png'
    img9 = '90%.png'
    img10 = '100%.png'
        
