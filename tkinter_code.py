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

        self.frames = {}

        container.grid_rowconfigure or .grid_columnconfigure or .grid_packconfigure #backbone of page switching function 

        for i in (frame1, frame2, frame3): #change framex to whatever class we created for each frame
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row = 1, column = 1) # change the grid numbers

    def show_frame(self, x):
        frame = self.frames[x]
        # next line depends on how we are going about it

        frame.#something = self.frames



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

