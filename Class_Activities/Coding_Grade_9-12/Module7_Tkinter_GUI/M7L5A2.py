# Module 7 Lesson 5 Activity 2: Denomination Calculator
# A GUI application using Toplevel, nested functions, floor division, modulo, and try/except

import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# -------------------------------
# Setting up Main Window
# -------------------------------
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

# -------------------------------
# Adding Image and Labels in Main Window
# -------------------------------
img_path = os.path.join(os.path.dirname(__file__), "app_img.jpg")
if not os.path.exists(img_path):
    img_path = "app_img.jpg"

upload = Image.open(img_path)
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue",
    font=("Arial", 11, "bold")
)
label1.place(relx=0.5, y=335, anchor=CENTER)

# -------------------------------
# Function to open messagebox
# -------------------------------
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

# -------------------------------
# Adding Button in Main Window
# -------------------------------
button1 = Button(
    root, text="Let's get started!", command=msg, bg="brown", fg="white"
)
button1.place(x=260, y=360)

# -------------------------------
# Function for opening new/top window
# -------------------------------
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light grey", font=("Arial", 11))
    entry = Entry(top, width=25)
    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey",
        font=("Arial", 11, "bold")
    )
    l1 = Label(top, text="2000", bg="light grey", font=("Arial", 10, "bold"))
    l2 = Label(top, text="500", bg="light grey", font=("Arial", 10, "bold"))
    l3 = Label(top, text="100", bg="light grey", font=("Arial", 10, "bold"))
    t1 = Entry(top, width=15)
    t2 = Entry(top, width=15)
    t3 = Entry(top, width=15)

    # -------------------------------
    # Calculation Function (Nested)
    # -------------------------------
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
        top, text="Calculate", command=calculator, bg="brown", fg="white"
    )

    # -------------------------------
    # Placing Widgets with place()
    # -------------------------------
    label.place(x=230, y=45)
    entry.place(x=225, y=75)
    btn.place(x=260, y=115)
    lbl.place(x=130, y=165)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

# -------------------------------
# Start Main Loop
# -------------------------------
root.mainloop()
