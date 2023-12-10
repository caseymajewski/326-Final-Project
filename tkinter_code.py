from tkinter import *
import tkinter as tk

# multiple screens: multiple classes and each class is a "page" (frame) and then have a button that flips from one page to another, but also have a main class for the main part of it. 
# when you put in a button you add in a commmand and a controller and then the command says if you click it it'll show frame and the parameters are classes that represent diff pages. Instead of a button,
# you would have
# have a counter and a sum and every time the sum equals a certain amount it goes to a new page, counter adds however much water the user drank. 
# coding syntax: import tkinter as tk

# inside of the specific page you are making, make the main class the home page, inside init function of each class (frame/page), use this as it defines what is happening on this page
# need a function that changes between each frame on the main page, the main page is the one you are going to be going back and forth from

# Tkinter.Button(self, text = "cups of water", command = lambda: controller.show_frame(Tkinter))

#syntax for switching frames

# this class basically inherits from the tkinter module as a subclass of the tkinter, which is why there are parameters in the class
class MainPage(tk.Tk):

    #Thompson helped us with this plzzzz
    def __init__(self, *args, **kwargs): #asteriks are shortcuts, normally would pass in variables, instead of limiting to just x,y you can do asterik args which takes in a sample argument. Think of SQL, * allow you to put an unlimited amount of variables in there. Ifyou were to do the sum of *args and pass in 3 numbers it will add 3 numbers together. Keywords of args and kwargs mean: args stand for argument and kwargs stand for keyword arguments.

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row = 1, column = 1)

        self.frames = {}

        #container.grid_rowconfigure or .grid_columnconfigure or .grid_packconfigure #backbone of page switching function 

        for f in (Frame1, Frame2): #frame3): #change framex to whatever class we created for each frame
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 1, column = 1, sticky = "nsew") # sticky determines where to position the widget in its cell, and the string contains n = north, s = south, e = east, w = west

    def show_frame(self, controller):
        '''Function designed to switch between frames in tkinter. '''

        frame = self.frames[controller]
        frame.tkraise()
        # next line depends on how we are going about it

class Frame1(tk.Frame):
    ''' Homepage'''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.load_images()

        # is there a way for us to use inheritance here as well? the only thing that changes between classes is the button takes you to the next frame in the sequence
        button = tk.Button(self, command = lambda: controller.show_frame(Frame2))

        button.grid(row = 1, column = 0, pady = 10, padx = 10)

    def load_image(self):

        image_path = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/MainPage().png"

        self.image = PhotoImage(file = image_path)


class Frame2(Frame1):
    '''Info Page (Enter your information below). '''
    # we need to add more for this one than others because it takes user input so likely needs more than just a button

    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        image_path_2 = "C:/Users/casey/OneDrive/Documents/GitHub/326-Final-Project/Info.png"
        self.load_image(image_path_2)

        button2 = tk.Button(self, command = lambda: controller.show_frame(Frame3))
        button2.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame3(Frame1):
    '''Log Water Screen (takes you to 10%)'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_3 = ""
        self.load_image(image_path_3)

        button3 = tk.Button(self, command = lambda: controller.show_frame(Frame4))
        button3.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame4(Frame1):
    '''10% there'''

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_4 = ""
        self.load_image(image_path_4)

        button4 = tk.Button(self, command = lambda: controller.show_frame(Frame5))
        button4.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame5(Frame1):
    '''20% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_5 = ""
        self.load_image(image_path_5)

        button5 = tk.Button(self, command = lambda: controller.show_frame(Frame6))
        button5.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame6(Frame1):
    '''30% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_6 = ""
        self.load_image(image_path_6)

        button6 = tk.Button(self, command = lambda: controller.show_frame(Frame7))
        button6.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame7(Frame1):
    '''40% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_7 = ""
        self.load_image(image_path_7)

        button7 = tk.Button(self, command = lambda: controller.show_frame(Frame8))
        button7.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame8(Frame1):
    '''50% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_8 = ""
        self.load_image(image_path_8)

        button8 = tk.Button(self, command = lambda: controller.show_frame(Frame9))
        button8.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame9(Frame1):
    '''60% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_9 = ""
        self.load_image(image_path_9)

        button9 = tk.Button(self, command = lambda: controller.show_frame(Frame10))
        button9.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame10(Frame1):
    '''70% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_10 = ""
        self.load_image(image_path_10)

        button10 = tk.Button(self, command = lambda: controller.show_frame(Frame11))
        button10.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame11(Frame1):
    '''80% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_11 = ""
        self.load_image(image_path_11)

        button11 = tk.Button(self, command = lambda: controller.show_frame(Frame12))
        button11.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame12(Frame1):
    '''80% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_12 = ""
        self.load_image(image_path_12)

        button12 = tk.Button(self, command = lambda: controller.show_frame(Frame13))
        button12.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame13(Frame1):
    '''90% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_13 = ""
        self.load_image(image_path_13)

        button13 = tk.Button(self, command = lambda: controller.show_frame(Frame14))
        button13.grid(row = 1, column = 0, pady = 10, padx = 10)

class Frame14(Frame1):
    '''100% there'''
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        image_path_14 = ""
        self.load_image(image_path_14)

        button14 = tk.Button(self, command = lambda: controller.show_frame(Frame15))
        button14.grid(row = 1, column = 0, pady = 10, padx = 10)


if __name__ == "__main__":

    main = MainPage()
    main.geometry("400x300")
    main.mainloop()

'''class Tkinter():

    def __init__(self, screenname, basename, classname, usetk, sync, use):

        self.screenname = None
        self.basename = None
        self.classname = 'Tk'
        self.usetk = True
        self.sync = False
        self.use = None
    
    def widget(self):

        # before we do anything else we have to create the window that pops up

        # root widget set equal to tk()
        root = Tk()

        # creating label widget
        myLabel = Label(root, text = "Welcome to Terrapin Water Tracker")

        # puts label on the screen
        myLabel.pack 

        # our root widget is included in the main loop of the program
        root.mainloop()
'''

