from tkinter import Tk, Frame, simpledialog, messagebox, Label, Button
from button import ImageButtonApp  
from PIL import ImageTk, Image

class WaterCalculator:
    
    def __init__(self):
        self.bmr = None
        self.TDEE = None
        self.water_goal = None
        self.get_user_input()

    def get_user_input(self):
        self.age = simpledialog.askinteger("Input", "Enter your age:")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")
        self.calculate_goals()

    def calculate_goals(self):
        self.calc_BMR()  # Calculate BMR
        self.adjust_for_activity_level()  # Adjust BMR based on activity level
        self.water_goal = self.final_intake()  # Now set the water goal
        messagebox.showinfo("Daily Water Goal", f"Your daily water intake goal is {self.water_goal:.2f} ounces.")

    def calc_BMR(self):
        if self.sex == "m":
            self.bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif self.sex == "f":
            self.bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'm' or 'f'.")
        return self.bmr

    def adjust_for_activity_level(self):
        activity_multipliers = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
        if self.activity_level in activity_multipliers:
            self.TDEE = self.bmr * activity_multipliers[self.activity_level]
        else:
            raise ValueError("Invalid value for 'activity_level'. Please use values 1-5.")
        return self.TDEE

    def final_intake(self):
        water_intake_goal_oz = self.TDEE * 0.03
        return water_intake_goal_oz

class WaterTracker(WaterCalculator):
    """ Class tracking the water intake of the user"""
    def __init__(self):
        """Initializing the Water Tracker Class"""
        super().__init__()
        self.user_water_intake = 0

    def check_water_intake(self, user_water_intake):
        """Method tracking the user's water intake, calculating the percentage, and returning it
            Args:
                user_water_intake: the amount of water the user has drunk so far
            Returns:
                the percentage of the user's water intake goal that they have drunk so far"""
        self.user_water_intake += user_water_intake
        percentage = (self.user_water_intake / self.water_goal) * 100
        return percentage

class BenchmarkFrame(Frame):
    """Class representing a frame in the benchmarks"""
    def __init__(self, parent, water_tracker, index):
        """Initializes the Benchmark Frame Class
            Args:
                parent: represents the parent widget
                water_tracker: instance of water tracker class
                index: index of the benchmark # """
        super().__init__(parent)
        self.parent = parent
        self.water_tracker = water_tracker
        self.index = index

        # Button to record water intake
        self.drink_button = Button(self, text="I Drank Water", command=self.drink_water)
        self.drink_button.pack()

    def drink_water(self):
        """Provides pop up for user water intake input, and gets the appropriate frame"""
        user_water_intake = simpledialog.askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake:
            percentage = self.water_tracker.check_water_intake(user_water_intake)
            self.parent.update_image(percentage)


class MainPage(Tk):
    """Main Page for the Water Tracker"""
    def __init__(self, *args, **kwargs):
        """inititalizes the Main page Class
            Args:"""
        super().__init__(*args, **kwargs)
        self.title("Water Intake Tracker")
        self.water_tracker = WaterTracker()

        self.image_paths = ['0%.png', '10%.png', '20%.png', '30%.png', '40%.png', '50%.png', '60%.png', '70%.png', '80%.png', '90%.png', '100%.png']
        self.image_button_app = ImageButtonApp(self, self.image_paths, self.drink_water)
        self.image_button_app.grid(row=0, column=0, sticky="nsew")

        self.frames = {}
        for i in range(11):
            frame = BenchmarkFrame(self, self.water_tracker, i)
            self.frames[f"Benchmark{i}"] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        self.initial_image = ImageTk.PhotoImage(file=self.image_paths[0])
        self.label = Label(self, image=self.initial_image)
        self.label.grid(row=2, column=0, sticky="nsew")
        self.label.image = self.initial_image

    def drink_water(self):
        user_water_intake = simpledialog.askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake:
            percentage = self.water_tracker.check_water_intake(user_water_intake)
            self.update_image(percentage)

    def update_image(self, percentage):
        index = min(int(percentage // 10), len(self.image_paths) - 1)
        new_image = ImageTk.PhotoImage(file=self.image_paths[index])
        self.label.configure(image=new_image)
        self.label.image = new_image

if __name__ == "__main__":
    main = MainPage()
    main.mainloop()
