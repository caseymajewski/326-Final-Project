from tkinter import * as Tk
import pygame
from pygame.locals import *

pygame.init()

class TerrapinWaterTracker():

    def __init__(self, master):
            self.master = master
            self.master.title("Terrapin Water Tracker")
    
            self.screen= pygame.display.set_mode((800,600))
            pygame.display.set_caption(" Your Terrarium!")
            self.water_level=0
            self.age_var= StringVar()
            self.sex_var=StringVar()
            self.weight_var= StringVar()
            self.activity_level_var=IntVar()

            self.create_user_input_widgets


            self.label= tk .Label(master, text = "Terrapin Water Tracker")
            self.label.pack()
    
    def widget(self):

        # before we do anything else we have to create the window that pops up

        # root widget set equal to tk()
        root = Tk()

        # creating label widget
        myLabel = Label(root, text = "Welcome to Terrapin Water Tracker")

        # puts label on the screen
        myLabel.grid(row=0, column=0)

        # our root widget is included in the main loop of the program
        root.mainloop()

        start_button= Button( root, text ="Start", padx=50, pady=50)
        start_button.grid( row=7, column= 8)




