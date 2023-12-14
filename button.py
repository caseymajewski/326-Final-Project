'''from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class Button():
    def __init__(self):
        root = tk.Tk()

        root.geometry('1920x1080')
        frame = Frame(root)
        frame.pack()
        frame.place(anchor = 'center', relx= 0.5, rely = 0.5)

        img = ImageTk.PhotoImage(Image.open("20%.png"))

        label = Label(frame, image = img)
        label.pack()

        I_Drank_Water_btn = tk.Button(root, text = "I Drank Water")
        I_Drank_Water_btn.place(relx = 0.75, rely = 0.5, anchor = 'center')
        Exit = tk.Button(root, text = "Exit", command = root.destroy)
        Exit.pack()

        root.mainloop()

if __name__ == "__main__":
    b = Button()

'''

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class ImageButtonApp:
    def __init__(self, image_path):
        root = tk.Tk()

        root.geometry('1920x1080')
        frame = Frame(root)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        img = ImageTk.PhotoImage(Image.open(image_path))

        label = Label(frame, image=img)
        label.pack()

        I_Drank_Water_btn = tk.Button(frame, text="I Drank Water")
        I_Drank_Water_btn.place(relx=0.75, rely=0.5, anchor='center')

        Exit = tk.Button(frame, text="Exit", command=root.destroy)
        Exit.place(relx=0.75, rely=0.6, anchor='center')

        root.mainloop()
