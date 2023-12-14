from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

root.geometry('1920x1080')
Benchmark_2 = Frame(root)
Benchmark_2.pack()
Benchmark_2.place(anchor = 'center', relx= 0.5, rely = 0.5)

img = ImageTk.PhotoImage(Image.open("20%.png"))

label = Label(Benchmark_2, image = img)
label.pack()

I_Drank_Water_btn = tk.Button(root, text = "I Drank Water")
I_Drank_Water_btn.place(relx = 0.75, rely = 0.5, anchor = 'center')
Exit = tk.Button(root, text = "Exit", command = root.destroy)
Exit.pack()

root.mainloop()





'''btn = tk.Button(root, text = 'I Drank Water', bd = '5', command = root.destroy)

btn.pack(side = 'top')

root.mainloop()'''