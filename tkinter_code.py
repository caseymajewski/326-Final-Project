from tkinter import *

# multiple screens: multiple classes and each class is a "page" (frame) and then have a button that flips from one page to another, but also have a main class for the main part of it. 
# when you put in a button you add in a commmand and a controller and then the command says if you click it it'll show frame and the parameters are classes that represent diff pages. Instead of a button,
# you would have
# have a counter and a sum and every time the sum equals a certain amount it goes to a new page, counter adds however much water the user drank. 
# coding syntax: import tkinter as tk

# inside of the specific page you are making, make the main class the home page, inside init function of each class (frame/page), use this as it defines what is happening on this page
# need a function that changes between each frame on the main page, the main page is the one you are going to be going back and forth from
Tkinter.Button(self, text = "cups of water", command = lambda: controller.show_frame(Tkinter))
class Tkinter():

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


