from tkinter import Tk, Frame, simpledialog, messagebox, Label
from button import ImageButtonApp  
from PIL import ImageTk, Image

class WaterCalculator:
    def __init__(self):
        self.bmr = None
        self.TDEE = None
        self.get_user_input()

    def get_user_input(self):
        self.age = simpledialog.askinteger("Input", "Enter your age:")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")

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
    def __init__(self):
        super().__init__()
        self.calc_BMR() # Calculate BMR
        self.adjust_for_activity_level() # Adjust BMR based on activity level
        self.water_goal = self.final_intake() # Now set the water goal
        self.user_water_intake = 0

    def check_water_intake(self, user_water_intake):
        self.user_water_intake += user_water_intake
        if self.user_water_intake >= self.water_goal:
            messagebox.showinfo("Congratulations!", "You have met your daily water goal.")
        else:
            messagebox.showinfo("Keep Going!", f"You need to drink {self.water_goal - self.user_water_intake:.2f} more ounces of water to reach your goal.")

class BenchmarkFrame(Frame):
    def __init__(self, parent, water_tracker, index):
        super().__init__(parent)
        self.parent = parent
        self.water_tracker = water_tracker
        self.index = index

        # Use ImageButtonApp here
        self.image_button = ImageButtonApp(self, f"{index * 10}%.png", self.drink_water)
        self.image_button.pack()

    def drink_water(self):
        user_water_intake = simpledialog.askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake:
            self.water_tracker.check_water_intake(user_water_intake)
            self.parent.next_image() 

class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Water Intake Tracker")
        self.water_tracker = WaterTracker()

        image_paths= ['0%.png','10%.png','20%.png','30%.png','40%.png','50%.png','60%.png','70%.png','80%.png','90%.png','100%.png']
        self.image_button_app = ImageButtonApp(self, image_paths)
        self.image_button_app.pack(expand=True, fill='both')

        self.frames = {}
        self.image_index = 0
        self.image_paths = [f"{i * 10}%.png" for i in range(11)]  # List of image paths

        for i in range(11):
            frame = BenchmarkFrame(self, self.water_tracker, i)
            self.frames[f"Benchmark{i}"] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.label = Label(self, image=ImageTk.PhotoImage(file=self.image_paths[self.image_index]))
        self.label.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Benchmark0")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.image_paths)
        new_image = ImageTk.PhotoImage(file=self.image_paths[self.image_index])
        self.label.configure(image=new_image)
        self.label.image = new_image  # Keep a reference

if __name__ == "__main__":
    main = MainPage()
    main.mainloop()
