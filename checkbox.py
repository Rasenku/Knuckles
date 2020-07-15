from tkinter import *
from tkinter import ttk

window = Tk()

var = IntVar()
showPath = ttk.Checkbutton(window, text='Show Steps :', onvalue=1, offvalue=0, variable=var)
showPath.grid(row=1, pady=3)
mainloop()

if var.get():
    print("Hello, World!")
else:
    print("Good Bye")