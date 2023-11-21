from tkinter import *

# before we do anything else we have to create the window that pops up

# root widget set equal to tk()
root = Tk()

# creating label widget
myLabel = Label(root, text = "Welcome to Terrapin Water Tracker")

# puts label on the screen
myLabel.pack 

# our root widget is included in the main loop of the program
root.mainloop()