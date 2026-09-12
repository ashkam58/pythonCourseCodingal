# Module 7 Lesson 4 Activity 1: My Text Editor
# Build a functional text editor application with Tkinter using file dialogs and grid layout

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")

# Configure grid resizing
# Column 1 holds the text editor, so column 1 gets weight=1 to expand
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    txt_edit.delete(1.0, END)
    # Read contents of the input file and display in editor
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)

    window.title(f"Codingal's Text Editor - {filepath}")

# Function to Save a file
def save_file():
    """Save the current text as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

    window.title(f"Codingal's Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

# Position widgets inside frame and window with grid()
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()
