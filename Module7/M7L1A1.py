# M7L1A1: Tkinter Window (Pygame Window)
# Activity 1: Creating a basic Tkinter GUI window, setting title, geometry, and starting the mainloop

# Import necessary libraries
from tkinter import *

# Create Window
window = Tk()

# Set the window Title and Geometry
window.title('Demo Window')
window.geometry('400x300')

# Start the GUI event loop
# mainloop() keeps the window visible and responsive to events
window.mainloop()
