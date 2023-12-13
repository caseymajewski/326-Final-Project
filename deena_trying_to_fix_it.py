from tkinter import *
import tkinter as tk
import terrarium as t

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row=1, column=1)

        self.frames = {}

        # Create instances of frames and add them to the frames dictionary
        for F in (Frame1, InfoPage, Water_Calculator_Screen, Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        # Show the initial frame
        self.show_frame(Frame1)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

        # Create and add a Start button to the GUI
        start_button = Button(self, text="Start", padx=50, pady=50, command=lambda: self.trigger_terrarium())
        start_button.grid(row=7, column=8)

    def trigger_terrarium(self):
        # Call the necessary terrarium functions or logic here
        t.Water_Calculator().get_user_input()


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.load_image()

    def load_image(self):
        image_path = "MainPage.png"
        self.image = PhotoImage(file=image_path)


class InfoPage(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)


class Water_Calculator_Screen(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_wc = ""
        self.load_image(image_path_wc)

class Benchmark1(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_4 = "10%.png"
        self.load_image(image_path_4)
        self.button()

class Benchmark2(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_5 = "20%.png"
        self.load_image(image_path_5)
        self.button()

class Benchmark3(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_6 = "30%.png"
        self.load_image(image_path_6)
        self.button()

class Benchmark4(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_7 = "40%.png"
        self.load_image(image_path_7)
        self.button()

class Benchmark5(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_8 = "50%.png"
        self.load_image(image_path_8)
        self.button()

class Benchmark6(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_9 = "60%.png"
        self.load_image(image_path_9)
        self.button()

class Benchmark7(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_10 = "70%.png"
        self.load_image(image_path_10)
        self.button()

class Benchmark8(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_11 = "80%.png"
        self.load_image(image_path_11)
        self.button()

class Benchmark9(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_12 = "90%.png"
        self.load_image(image_path_12)
        self.button()

class Benchmark10(Frame1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_14 = "100%.png"
        self.load_image(image_path_14)
        self.button()

if __name__ == "__main__":
    main = MainPage()
