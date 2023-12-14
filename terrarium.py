from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askfloat
from tkinter import Frame, PhotoImage, Button
from button import Button
from tkinter import messagebox
class  Water_Calculator():

    def __init__(self):
        """Initialize the Calculator class.
        Args: 
            self
            """
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
    #so then we delete this? ^^^

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
        water_intake_oz = self.TDEE * 0.03
        water_intake_cups = water_intake_oz * 0.125
        message = f"Your daily water goal is {water_intake_oz:.2f} ounces, or {water_intake_cups:.2f} cups!"
        self.water_goal= water_intake_oz

        # Show the message in a popup
        messagebox.showinfo("Water Intake Result", message) #not recognizing messagebox for some reason
        return self.water_goal


class WaterTracker(Water_Calculator):

    def __init__(self):
        """Initialize the WaterTracker class."""
        super().__init__()        

    def check_water_intake(self):
        """
        Check the water intake for the user.

        Parameters:
        amount (float): The amount of water the user drank today.
        """
        # Initialize the user's water intake to zero
        self.user_water_intake = 0
        # Loop until the user's water intake is equal or greater than the target water intake
        while self.user_water_intake < self.water_goal:
            # Ask the user how much water they have drank today
            try:
                amount+= float(input("How much water have you drank today?: "))
                self.user_water_intake += amount
            # Compare the user's water intake with the target water intake            
                percentage = round((self.user_water_intake / self.water_goal) * 100, -1)
                if percentage >= 100:
                    print("Congratulations! You have met your daily water goal.")
                else: 
                    print(f"Keep Going! You only drank {percentage}% of your daily water goal) /n You need to drink {self.user_water_intake - self.user_water_intake} more ounces of water to reach your goal")
            except ValueError: 
                print("Invalid Input. Please enter a numeric value!")
    def update_terrarium_water_level(self, amount, percentage):
        """
        Update the water level in the terrarium.

        Parameters:
        amount (float): The amount of water to update the terrarium water level with.
        percentage (float): The percentage of the water goal achieved by the user.
        """
        frame_index = int(percentage / 10)  # Assuming 10% intervals
        benchmark_name = f"Benchmark{frame_index}"
        frame = self.get(benchmark_name)

        amount=0
        

        if frame:
            # Update the water level in the corresponding frame
            frame.update_water_level(amount)  # Pass the amount parameter to the method
        else:
            print(f"Unable to find the corresponding frame for percentage {percentage}%.")
    
    def get_benchmark_class(self, percentage):
        frame_index = int(percentage / 10)  # Assuming 10% intervals
        benchmark_name = f"Benchmark{frame_index}"
        return self.frames.get(benchmark_name)


class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.grid(row=1, column=1)

        # Create an instance of WaterTracker with the calculated water goal
        self.water_tracker = WaterTracker()
        self.Water_Calculator= Water_Calculator

        # Create instances of frames and add them to the frames dictionary
        if self.water_tracker.user_water_intake < self.Water_Calculator.final_intake():
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
            if 90.1 <= water_intake and water_intake <= 10:
                return Benchmark9
        
            
        
            
            
        
        

        
        
        
        
        
        
        
        
        
    
        '''for f in (Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self, self.water_tracker)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")'''

        # Show the initial frame (change this to the desired initial frame)
        self.show_frame(Benchmark1)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

class Benchmark0(Frame):
    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        
        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(user_water_intake)
       
class Benchmark1(Frame):
    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        
        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(user_water_intake)
       

        # Transition to the corresponding benchmark
        if benchmark_class:
            self.controller.show_frame(benchmark_class.__name__)
        else:
            print(f"Unable to find the corresponding benchmark for percentage {percentage}%.")

class Benchmark2(Benchmark1): 
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_5 = "20%.png"
        self.load_image(image_path_5)

class Benchmark3(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_6 = "30%.png"
        self.load_image(image_path_6)
        self.button()

class Benchmark4(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_7 = "40%.png"
        self.load_image(image_path_7)
        self.button()

class Benchmark5(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_8 = "50%.png"
        self.load_image(image_path_8)
        self.button()

class Benchmark6(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_9 = "60%.png"
        self.load_image(image_path_9)
        self.button()

class Benchmark7(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_10 = "70%.png"
        self.load_image(image_path_10)
        self.button()

class Benchmark8(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_11 = "80%.png"
        self.load_image(image_path_11)
        self.button()

class Benchmark9(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_12 = "90%.png"
        self.load_image(image_path_12)
        self.button()

class Benchmark10(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        image_path_14 = "100%.png"
        self.load_image(image_path_14)
        self.button()

if __name__ == "__main__":
    main = MainPage()
    main.mainloop()
