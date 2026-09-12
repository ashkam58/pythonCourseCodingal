# Module 7 Lesson 5 Activity 1: Let's Top a Window
# Learn how to create and configure a secondary Toplevel window in Tkinter

from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    # Adding a label widget to Top Window
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text="This is root window")
btn = Button(root, text="click here to open another window", command=topwin)

# Arranging widgets
l.pack()
btn.pack()

# Start main GUI event loop
root.mainloop()
