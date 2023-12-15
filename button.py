from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class ImageButtonApp:
    def __init__(self, image_paths):
        self.root = tk.Tk()
        self.root.geometry('1920x1080')

        self.frame = Frame(self.root)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        self.image_paths = image_paths
        self.image_index = 0

        self.img = ImageTk.PhotoImage(Image.open(self.image_paths[self.image_index]))
        self.label = Label(self.frame, image=self.img)
        self.label.pack()

        self.drink_water_button = tk.Button(self.frame, text="I Drank Water", fg='#FFCCCB', bg='#CB3737', font=("Times New Roman Bold", 18), command=self.next_image)
        self.drink_water_button.pack()
        self.drink_water_button.place(relheight=.12, relwidth=0.2, relx=0.90, rely=0.5, anchor='center')

        self.exit_button = tk.Button(self.frame, text="Exit", fg='#FFCCCB', bg='#CB3737', font=("Times New Roman Bold", 10), command=self.root.destroy)
        self.exit_button.place(relx=0.90, rely=0.6, anchor='center')

        self.root.mainloop()

    def next_image(self):
        # Increment the index
        self.image_index = (self.image_index + 1) % len(self.image_paths)
        # Update the image
        self.img = ImageTk.PhotoImage(Image.open(self.image_paths[self.image_index]))
        self.label.configure(image=self.img)
        self.label.image = self.img  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    image_paths = ['10%.png', '20%.png', '30%.png', '40%.png', '50%.png', '60%.png', '70%.png', '80%.png', '90%.png', '100%.png']  # Update with your actual paths
    app = ImageButtonApp(image_paths)
