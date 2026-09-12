# M7L2A1: Number Pad
# Activity 1: Creating a visual number pad using Frame, relief=SUNKEN, grid layout, and nested loops

# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

# 2D list storing the keypad's numbers and symbols
nums = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ['#', 0, '*']
]

# Outer loop: Iterate through 4 rows
for i in range(4):
    # Configure rows and columns to resize window evenly
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

    # Inner loop: Iterate through 3 columns
    for j in range(0, 3):
        # Create a Frame for each cell with a 3D SUNKEN border
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j)

        # Create a Label inside each frame displaying the number/symbol
        label = Label(master=frame, text=nums[i][j], bg='#d0efff')
        label.pack(padx=3, pady=3)

# Start the GUI event loop
root.mainloop()
