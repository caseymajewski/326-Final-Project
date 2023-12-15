# button.py
import tkinter as tk
from PIL import ImageTk, Image

class ImageButtonApp(tk.Frame):
    def __init__(self, parent, image_paths, drink_water_command, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.image_paths = image_paths
        self.image_index = 0

        self.drink_water_button = tk.Button(self, text="I Drank Water", fg='#FFCCCB', bg='#CB3737', font=("Times New Roman Bold", 18), command=drink_water_command)
        self.drink_water_button.pack()
        self.drink_water_button.place(relheight=.12, relwidth=0.2, relx=0.90, rely=0.5, anchor='center')

        self.exit_button = tk.Button(self, text="Exit", fg='#FFCCCB', bg='#CB3737', font=("Times New Roman Bold", 10), command=self.parent.destroy)
        self.exit_button.place(relx=0.90, rely=0.6, anchor='center')

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.image_paths)
        self.img = ImageTk.PhotoImage(Image.open(self.image_paths[self.image_index]))
        self.label.configure(image=self.img)
        self.label.image = self.img
