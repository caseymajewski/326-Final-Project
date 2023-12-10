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

# this class basically inherits from the tkinter module as a subclass of the tkinter, which is why there are parameters in the class
class MainPage(tk.Tk):

    #Thompson helped us with this 
    def __init__(self, *args, **kwargs): #asteriks are shortcuts, normally would pass in variables, instead of limiting to just x,y you can do asterik args which takes in a sample argument. Think of SQL, * allow you to put an unlimited amount of variables in there. Ifyou were to do the sum of *args and pass in 3 numbers it will add 3 numbers together. Keywords of args and kwargs mean: args stand for argument and kwargs stand for keyword arguments.

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row = 1, column = 1)

        self.frames = {}

        #container.grid_rowconfigure or .grid_columnconfigure or .grid_packconfigure #backbone of page switching function

        for f in (Frame1, InfoPage, I_Drank_Water_Screen, Water_Calculator_Screen, Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10): #frame3): #change framex to whatever class we created for each frame
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 1, column = 1, sticky = "nsew") # sticky determines where to position the widget in its cell, and the string contains n = north, s = south, e = east, w = west

    def show_frame(self, controller):
        '''Function designed to switch between frames in tkinter. '''

        frame = self.frames[controller]
        frame.tkraise()
        # next line depends on how we are going about it

        start_button= Button( root, text ="Start", padx=50, pady=50)
        start_button.grid( row=7, column= 8)


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

        # need to add code here that saves the user input to the backend for the program to keep in mind for the daily water intake goal


class I_Drank_Water_Screen(Frame1):
    '''Log Water Screen (takes you to water calculator screen)'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_3 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/I Drank Water.png"
        self.load_image(image_path_3)

        self.button()

class Water_Calculator_Screen(Frame1):
    ''' Water Calculator page'''
    # QUESTION FOR TA: !!!!!!!! we need to add some sort of user input here as well as it is the screen that will update on the backend

    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        image_path_wc = ""
        self.load_image(image_path_wc)

class Benchmark1(Frame1):
    '''10% there'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_4 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/10%.png"
        self.load_image(image_path_4)

        self.button()

class Benchmark2(Frame1):
    '''20% there'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_5 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/20%.png"
        self.load_image(image_path_5)

        self.button()

class Benchmark3(Frame1):
    '''30% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_6 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/30%.png"
        self.load_image(image_path_6)

        self.button()

class Benchmark4(Frame1):
    '''40% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_7 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/40%.png"
        self.load_image(image_path_7)

        self.button()

class Benchmark5(Frame1):
    '''50% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_8 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/50%.png"
        self.load_image(image_path_8)

        self.button()

class Benchmark6(Frame1):
    '''60% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_9 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/60%.png"
        self.load_image(image_path_9)

        self.button()

class Benchmark7(Frame1):
    '''70% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_10 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/70%.png"
        self.load_image(image_path_10)

        self.button()

class Benchmark8(Frame1):
    '''80% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_11 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/80%.png"
        self.load_image(image_path_11)

        self.button()

class Benchmark9(Frame1):
    '''90% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_12 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/90%.png"
        self.load_image(image_path_12)

        self.button()

class Benchmark10(Frame1):
    '''100% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_14 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/100%.png"
        self.load_image(image_path_14)

if __name__ == "__main__":
    main = MainPage()
    main.geometry("400x300")
    main.mainloop()

calculator = Water_Calculator()
calculator.calc_BMR()
calculator.adjust_for_activity_level()
calculator.final_intake()