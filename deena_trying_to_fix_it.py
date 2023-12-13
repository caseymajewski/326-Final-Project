from tkinter import *
import tkinter as tk
import terrarium as t

class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.grid(row=1, column=1)

        self.frames = {}

        # Create instances of frames and add them to the frames dictionary
        for F in (Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        # Show the initial frame (change this to the desired initial frame)
        self.show_frame(Benchmark1)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

        # Create and add a Start button to the GUI
        start_button = Button(self, text="Start", padx=50, pady=50, command=lambda: self.show_frame(InfoPopUp))
        start_button.grid(row=7, column=8)
class Benchmark1(Frame):
    ''' Homepage'''

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.load_image()

    def load_image(self, image_path="MainPage.png"):
        self.image = PhotoImage(file=image_path)



class Benchmark2(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_5 = "20%.png"
        self.load_image(image_path_5)
        self.button()

class Benchmark3(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_6 = "30%.png"
        self.load_image(image_path_6)
        self.button()

class Benchmark4(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_7 = "40%.png"
        self.load_image(image_path_7)
        self.button()

class Benchmark5(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_8 = "50%.png"
        self.load_image(image_path_8)
        self.button()

class Benchmark6(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_9 = "60%.png"
        self.load_image(image_path_9)
        self.button()

class Benchmark7(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_10 = "70%.png"
        self.load_image(image_path_10)
        self.button()

class Benchmark8(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_11 = "80%.png"
        self.load_image(image_path_11)
        self.button()

class Benchmark9(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_12 = "90%.png"
        self.load_image(image_path_12)
        self.button()

class Benchmark10(Benchmark1):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        image_path_14 = "100%.png"
        self.load_image(image_path_14)
        self.button()

if __name__ == "__main__":
    main = MainPage()
