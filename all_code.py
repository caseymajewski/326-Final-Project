from tkinter import Tk, Frame, Button, simpledialog, messagebox
from terrarium import WaterTracker
from tkinter.simpledialog import askfloat
from tkinter import PhotoImage


class WaterCalculator:
    def __init__(self):
        self.get_user_input()
        self.bmr = None
        self.TDEE = None

    def get_user_input(self):
        try:
            self.age = simpledialog.askinteger("Input", "Enter your age:")
            self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):").lower()
            self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
            self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
            self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input. Please try again.")
            self.get_user_input()

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
        water_intake_oz = self.TDEE * 0.03
        water_intake_cups = water_intake_oz * 0.125
        message = f"Your daily water goal is {water_intake_oz:.2f} ounces, or {water_intake_cups:.2f} cups!"
        messagebox.showinfo("Water Intake Result", message)


class WaterTrackerWithButton(WaterTracker):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_page = main_page
        self.calc_BMR()  # Calculate BMR
        self.adjust_for_activity_level()  # Adjust for activity level

    def show_drank_water_button(self):
        self.main_page.frames[Benchmark1].show_drank_water_button()

    def check_water_intake(self, amount):
        self.user_water_intake += amount

        if self.user_water_intake >= self.water_goal:
            print("Congratulations! You have met your daily water goal.")
            percentage = round((self.user_water_intake / self.water_goal) * 100, -1)
            self.update_terrarium_water_level(amount, percentage)

            benchmark_class = self.get_benchmark_class(percentage)

            if benchmark_class:
                self.main_page.show_frame(benchmark_class.__name__)
            else:
                print(f"Unable to find the corresponding benchmark for percentage {percentage}%.")
        else:
            print(f"You need to drink {self.water_goal - self.user_water_intake} more ounces of water to reach your goal.")

class MainPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = Frame(self)
        container.grid(row=1, column=1)
        self.frames = {}

        self.water_tracker = WaterTrackerWithButton(self)

        for F in (Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self, self.water_tracker)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        self.show_frame(Benchmark1)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class Benchmark1(Frame):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent)
        self.water_tracker = water_tracker
        self.drank_water_button = Button(self, text="I drank water", command=self.drink_water, state="disabled")
        self.drank_water_button.pack()

    def show_drank_water_button(self):
        self.drank_water_button.config(state="normal")

    def drink_water(self):
        user_water_intake = askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake is not None:  # Check if the user clicked "Cancel"
            self.water_tracker.check_water_intake(user_water_intake)


    class Benchmark2(Benchmark1):
            def __init__(self, parent, controller, water_tracker):
                super().__init__(parent, controller, water_tracker)
                self.load_image("20%.png")
                image_path="20%.png"

            def load_image(self, image_path):
                image = PhotoImage(file=image_path)


class Benchmark3(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("30%.png")
        self.button()


class Benchmark4(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("40%.png")
        self.button()


class Benchmark5(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("50%.png")
        self.button()


class Benchmark6(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("60%.png")
        self.button()


class Benchmark7(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("70%.png")
        self.button()


class Benchmark8(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("80%.png")
        self.button()


class Benchmark9(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("90%.png")
        self.button()


class Benchmark10(Benchmark1):
    def __init__(self, parent, controller, water_tracker):
        super().__init__(parent, controller, water_tracker)
        self.load_image("100%.png")
        self.button()


if __name__ == "__main__":
    main = MainPage()
    main.mainloop()
