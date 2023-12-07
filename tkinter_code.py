from tkinter import *

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


