# M7L3A2: Virus Detected
# Activity 2: Displaying popup warning dialogs using messagebox.showwarning and Button command

# Import necessary libraries
from tkinter import *
from tkinter import messagebox  # Must be explicitly imported!

# Setup Tkinter Window
root = Tk()
root.title("Virus Scanner")
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked (takes 0 arguments when used with command=)
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
