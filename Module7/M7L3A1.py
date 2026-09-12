# M7L3A1: Event Handler
# Activity 1: Handling keypress (<Key>) and mouse click (<Button-1>) events using .bind()

# Import necessary libraries
from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# Event Handler for Keypress
def handle_keypress(event):
    """Print the character associated to the key pressed."""
    print(event.char)

# Bind keypress event to handle_keypress() on the main window
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    """Print message when the button is clicked."""
    print("\nThe button was clicked!")

# Create Button widget
button = Button(text="Click me!")
button.pack()

# Bind left-click event (<Button-1>) directly to the button widget
button.bind("<Button-1>", handle_click)

# Start the GUI event loop
window.mainloop()
