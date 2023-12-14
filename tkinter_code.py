from tkinter import *
import tkinter as tk
import terrarium as t

# this class basically inherits from the tkinter module as a subclass of the tkinter, which is why there are parameters in the class
class MainPage(tk.Tk):

    #Thompson helped us with this plzzzz
    def __init__(self, *args, **kwargs): #asteriks are shortcuts, normally would pass in variables, instead of limiting to just x,y you can do asterik args which takes in a sample argument. Think of SQL, * allow you to put an unlimited amount of variables in there. Ifyou were to do the sum of *args and pass in 3 numbers it will add 3 numbers together. Keywords of args and kwargs mean: args stand for argument and kwargs stand for keyword arguments.

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row = 1, column = 1)

        self.frames = {}

        # simpledialog for text? 1920 x 1080 - default full screen
        button = tk.Button(self, command = lambda: controller.show_frame(Water_Calculator_PopUp))

        button.grid(row = 1, column = 0, pady = 10, padx = 10)
        #container.grid_rowconfigure or .grid_columnconfigure or .grid_packconfigure #backbone of page switching function

        # do if/else and a lot of conditionals here instead of a for loop because it makes more sense for the benchmark percentage range
        for f in (Frame1, InfoPopUp, Water_Calculator_PopUp, Benchmark1, Benchmark2, Benchmark3, Benchmark4, Benchmark5, Benchmark6, Benchmark7, Benchmark8, Benchmark9, Benchmark10): #frame3): #change framex to whatever class we created for each frame
            # input name of frame here i.e. InfoPage = input name of frame here i.e. InfoPage(container, self)
            self.frame# [input name of frame here i.e. InfoPage] = frame
            # input name of frame here i.e. InfoPage.grid(row = 1, column = 1, sticky = "nsew") # sticky determines where to position the widget in its cell, and the string contains n = north, s = south, e = east, w = west

    def show_frame(self, controller):
        '''Function designed to switch between frames in tkinter. '''

        frame = self.frames[controller]
        frame.tkraise()
        # next line depends on how we are going about it

        start_button= Button(root, text ="Start", padx=50, pady=50)
        start_button.grid( row=7, column= 8)


class Frame1(tk.Frame):

    ''' Homepage'''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.load_images()

    # QUESTION FOR TA: is this okay how it is or is there a way to make it case specific for each frame?
    def load_image(self):

        image_path = "MainPage.png"

        self.image = PhotoImage(file = image_path)


class InfoPopUp(Frame1):
    '''Info Pop Up (Enter your information below). '''

    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        t.Water_Calculator().get_user_input()


class Water_Calculator_PopUp(Frame1):
    ''' Water Calculator Pop Up'''
    # QUESTION FOR TA: !!!!!!!! we need to add some sort of user input here as well as it is the screen that will update on the backend

    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        image_path_wc = ""
        self.load_image(image_path_wc)

class Benchmark1(Frame1):
    '''10% there'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.image_app = ImageButtonApp(img)

        

class Benchmark2(Frame1):
    '''20% there'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_5 = "20%.png"
        self.load_image(image_path_5)

        self.button()

class Benchmark3(Frame1):
    '''30% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_6 = "30%.png"
        self.load_image(image_path_6)

        self.button()

class Benchmark4(Frame1):
    '''40% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_7 = "40%.png"
        self.load_image(image_path_7)

        self.button()

class Benchmark5(Frame1):
    '''50% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_8 = "50%.png"
        self.load_image(image_path_8)

        self.button()

class Benchmark6(Frame1):
    '''60% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_9 = "60%.png"
        self.load_image(image_path_9)

        self.button()

class Benchmark7(Frame1):
    '''70% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_10 = "70%.png"
        self.load_image(image_path_10)

        self.button()

class Benchmark8(Frame1):
    '''80% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_11 = "80%.png"
        self.load_image(image_path_11)

        self.button()

class Benchmark9(Frame1):
    '''90% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_12 = "90%.png"
        self.load_image(image_path_12)

        self.button()

class Benchmark10(Frame1):
    '''100% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_14 = "100%.png"
        self.load_image(image_path_14)

if __name__ == "__main__":
    main = MainPage()
    main.geometry("1920x1080")
    main.mainloop()

    img = Benchmark1('10%.png')
    img2 = Benchmark2('20%.png')
    img3 = Benchmark3('30%.png')
    img4 = Benchmark4('40%.png')
    img5 = Benchmark5('50%.png')
    img6 = Benchmark6('60%.png')
    img7 = Benchmark7('70%.png')
    img8 = Benchmark8('80%.png')
    img9 = Benchmark9('90%.png')
    img10 = Benchmark10('100%.png')