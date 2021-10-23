# This will go over the tkinter library for python
# $python3 -m tkinter # gives you an example window
# is imported like any other library
import tkinter as tk
from tkinter import scrolledtext, messagebox
import time
# we first will define the new window.
window = tk.Tk()
# gives a tab-title
window.title("Tester Window")
# frames are ment to hold content
window.Frame(window)
# essentailly a text box. fonts can be set too. .pack sets a block
window.Label(window, text="Hello, World", font=("Arial", 50)).pack()
# Entry is an input textbox
input = tk.Entry(window, width=20)
# positions our widget (objects in tkinter are known as widgets)
input.grid(column=0, row=1)
# combobox is a selector of multiple choices
combo = tk.Combobox(window)
# we define those values here as a tuple
combo.values(1, 2, 3, 4, 5, "Text")
# sets the defualt option
combo.current(3)
combo.grid(column=0, row=2)
# Spinbox is also a selector between a certain range
tk.Spinbox(window, from=0, to=100, width=5).grid(column=0, row=3)
# tk has it's own booleans
state = tk.BooleanVar()
state.set(True)
# and checkbuttons
check = tk.Checkbutton(window, text="select", var=state)
check.grid(column=0, row=4)
# radio buttons are accessed by unique values
window.Radiobutton(window, text="C/C++", value=3).grid(column=1,row=1)
window.Radiobutton(window, text="Javascript", value=2).grid(column=1,row=2)
window.Radiobutton(window, text="Python", value=1).grid(column=1,row=3)
window.Radiobutton(window, text="SASS/SCSS", value=4).grid(column=1,row=4)
window.Radiobutton(window, text="Go!", value=5).grid(column=1,row=5)
# scroll text box
scrolledtext.ScrolledText(window, width=50, height=50).place()
# message box
messagebox.showinfo("Message Title", "Message Content")
# command is used to name clicked function and must be defined before
# the button is created
def quite():
  # this reconfigures the text, changing it
  time.sleep(0.5)
  #then after 50ms destroys the program
  window.destroy()
  exit()
# creates a button
"""background and forground colors can be set too with bg="blue",
 fg="red. However, becuase mac does not support this color change,
 we have used highlightbackground="color" for the same purpose"""
window.Button(window, text="Quite!", command=quite, highlightbackground="#fcf").grid(column=1, row=2)
# Binding <Button-1> = left click, <Button-2> = middle click, <Button-3> = right click.
def click():
  window.Lable(window, text="Click!")
# it takes two parameters, the event and the function
window.bind("Button-1", click,highlightforeground="fcf")
# keeps the window running and must be placed at the end of yyour program
window.mainloop()
# for more checkout:
# https://youtu.be/VMP1oQOxfM0
# https://docs.python.org/3/library/tkinter.html
# This file doesn't compile... must be something wrong... 