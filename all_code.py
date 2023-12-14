from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askfloat
from tkinter import messagebox
from terrarium import WaterTracker 
from tkinter import Frame, PhotoImage, Button
from terrarium import WaterTracker, Water_Calculator
from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.simpledialog import askfloat
from terrarium import WaterTracker

class WaterCalculator:
    def __init__(self):
        """Initialize the Calculator class."""
        self.get_user_input()
        self.bmr = None
        self.TDEE = None

    def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        try:
            self.age = simpledialog.askinteger("Input", "Enter your age:")
            self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):").lower()
            self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
            self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
            self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")
        except (ValueError, TypeError):
            # Handle the case where the user clicks "Cancel" or enters invalid data
            print("Invalid input. Please try again.")
            self.get_user_input()

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
        water_goal = water_intake_oz

        # Show the message in a popup
        messagebox.showinfo("Water Intake Result", message)


class WaterTracker(Water_Calculator):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_page = main_page

    def check_water_intake(self, amount):
        """Check the water intake for the user."""
        # Calculate the user's total water intake
        self.user_water_intake += amount

        # Compare the user's water intake with the target water goal
        if self.user_water_intake >= self.water_goal:
            print("Congratulations! You have met your daily water goal.")
            # Calculate the percentage based on the user's total water intake and the water goal
            percentage = round((self.user_water_intake / self.water_goal) * 100, -1)
            # Update the terrarium water level
            self.update_terrarium_water_level(amount, percentage)

            # Get the benchmark class based on the current percentage
            benchmark_class = self.get_benchmark_class(percentage)

            # Transition to the corresponding benchmark
            if benchmark_class:
                self.main_page.show_frame(benchmark_class.__name__)
            else:
                print(f"Unable to find the corresponding benchmark for percentage {percentage}%.")
        else:
            print(f"You need to drink {self.water_goal - self.user_water_intake} more ounces of water to reach your goal.")


class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.grid(row=1, column=1)

        # Create an instance of WaterTrackerWithButton with the calculated water goal
        self.water_tracker = WaterTracker(self)

        # Create instances of frames and add them to the frames dictionary
        for F in (Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self, self.water_tracker)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        # Show the initial frame (change this to the desired initial frame)
        self.show_frame(Benchmark1)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class Benchmark1(Frame):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.water_tracker = water_tracker

        # Create a button for drinking water
        self.drink_water_button = Button(self, text="I drank water", command=self.drink_water)
        self.drink_water_button.pack()

    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")

        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(user_water_intake)




"""class Benchmark1(Frame):
    def drink_water(self):
        
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
            print(f"Unable to find the corresponding benchmark for percentage {percentage}%.")"""



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
