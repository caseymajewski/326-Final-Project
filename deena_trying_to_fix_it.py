from tkinter import *
import tkinter as tk
import terrarium as t
from tkinter.simpledialog import askfloat
from terrarium import WaterTracker 
from tkinter import Frame, PhotoImage, Button

class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.grid(row=1, column=1)

        # Create an instance of WaterTracker
        self.water_tracker = WaterTracker(water_goal=self.water_goal) 

        self.frames = {}

        # Create instances of frames and add them to the frames dictionary
        for F in (Benchmark1,Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self, self.water_tracker)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        # Show the initial frame (change this to the desired initial frame)
        self.show_frame(Benchmark1)

        # Create and add a Start button to the GUI
        """start_button = Button(self, text="Start", padx=50, pady=50, command=lambda: self.show_frame(Benchmark10))
        start_button.grid(row=7, column=8)"""

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

class Benchmark1(Frame):
    def drink_water(self):
        """Prompt the user to enter the amount of water they drank."""
        amount = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        
        # Call the WaterTracker's method to check water intake
        self.water_tracker.check_water_intake(amount)

        # Get the benchmark class based on the current percentage
        percentage = round((self.water_tracker.user_water_intake / self.water_tracker.water_goal) * 100, -1)
        benchmark_class = self.water_tracker.get_benchmark_class(percentage)

        # Transition to the corresponding benchmark
        if benchmark_class:
            self.controller.show_frame(benchmark_class)
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
