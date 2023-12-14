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

        I_Drank_Water_btn = tk.Button(frame, text="I Drank Water", fg = '#FFCCCB', bg = '#CB3737', font = ("Times New Roman Bold", 18))
        I_Drank_Water_btn.pack()
        I_Drank_Water_btn.place(relheight = .12, relwidth= 0.2, relx=0.90, rely=0.5, anchor='center')
        Exit = tk.Button(frame, text="Exit", fg = '#FFCCCB', bg = '#CB3737', font = ("Times New Roman Bold", 10), command=root.destroy)
        Exit.place(relx=0.90, rely=0.6, anchor='center')

        root.mainloop()

'''if __name__ == "__main__":
    image_path = '10%.png'  # Replace with the correct image file path
    app = ImageButtonApp(image_path)'''
