# Module 7: GUI Development with Tkinter
## Lesson 1: Widgets for Starters!

Welcome to **Module 7: GUI Development with Tkinter**! In this lesson, students transition from plain text console programs to real Graphical User Interfaces (GUIs). Students learn how to create desktop windows, arrange core widgets (**Label**, **Entry**, **Text**, **Button**), and manage the event loop with `mainloop()`.

---

## 📚 Overview & List of Topics

1. **What Is Tkinter and Importing It** (`from tkinter import *`)
2. **Creating a Window and Starting the Event Loop** (`Tk()`, `title()`, `geometry()`, `mainloop()`)
3. **Displaying Text with a Label Widget** (`Label()`, `pack()`, `fg`, `bg`)
4. **Getting Typed Input with an Entry Widget and `.get()`**
5. **Displaying Multi-Line Output with a Text Widget and `.insert()`**
6. **Connecting a Button's `command` to a Function** (`command=display` without parentheses)
7. **Activities & After Class Project (ACP)**

---

## 🔍 Topics in Detail

### 1. What Is Tkinter and Importing It
- **What it is:** Tkinter is Python's built-in GUI library. It ships with Python automatically, requiring no external `pip install`.
- **How it works:**
  ```python
  from tkinter import *
  ```
  This imports `Tk`, `Label`, `Button`, `Entry`, and `Text` directly into namespace without needing a `tkinter.` prefix.

### 2. Creating a Window and Starting the Event Loop
- **What it is:** Every GUI app requires one primary top-level window. `mainloop()` keeps the window responsive, listening for clicks and keystrokes.
- **How it works:**
  ```python
  window = Tk()
  window.title('Demo Window')
  window.geometry('400x300')  # Width x Height in pixels
  window.mainloop()            # MUST BE THE LAST LINE
  ```

### 3. Displaying Text with a Label Widget
- **What it is:** A non-interactive widget purely for showing headers, prompts, or status text.
- **How it works:**
  ```python
  lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
  lbl.pack()  # Must call pack() or widget remains invisible!
  ```

### 4. Getting Typed Input with an Entry Widget and `.get()`
- **What it is:** A single-line text input field.
- **How it works:**
  ```python
  name_entry = Entry()
  name_entry.pack()
  # Inside button callback function:
  user_name = name_entry.get()
  ```

### 5. Displaying Multi-Line Output with a Text Widget and `.insert()`
- **What it is:** A multi-line output container capable of displaying paragraphs, logs, or stacked messages.
- **How it works:**
  ```python
  text_box = Text(height=3)
  text_box.pack()
  # Inside button callback:
  text_box.delete(1.0, END)      # Clear existing content
  text_box.insert(END, "Hello!\n") # Append new content at END
  ```

### 6. Connecting a Button's `command` to a Function
- **What it is:** A clickable button widget wired to execute a custom Python function.
- **Critical Rule:** Write `command=display` **without parentheses**. Passing `command=display()` invokes the function at program startup instead of upon user click.
  ```python
  btn = Button(text="Begin", command=display, bg="#1261A0", fg="white")
  btn.pack()
  ```

---

## 📂 Lesson Activities & Files

| File | Type | Description |
|---|---|---|
| [`M7L1A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A1.py) | Activity 1 | Bare Tkinter GUI window setting title, geometry (400x300), and starting `mainloop()`. |
| [`M7L1A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A2.py) | Activity 2 | Getting started with widgets: Heading Label, Name Entry, Begin Button, and Text box output with current date. |
| [`M7L1ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1ACP.py) | After Class Project | Workshop Participant Greeting: Complete digital check-in desk with `delete(1.0, END)` clearing and multi-line formatting. |

---

## ⚠️ Common Beginner Traps & Solutions

1. **Window flashes and closes instantly:**
   - *Cause:* Missing `mainloop()` at the end of the script.
2. **Widget created but does not appear on screen:**
   - *Cause:* Forgot to call `.pack()` on the widget.
3. **Button triggers immediately when the script launches:**
   - *Cause:* Wrote `command=function()` with parentheses. Remove the `()`!
4. **`TypeError: insert() argument must be str`:**
   - *Cause:* Inserting `date.today()` directly into `text_box`. Always cast to string: `str(date.today())`.
5. **Repeated button clicks stack messages infinitely:**
   - *Cause:* Forgetting to clear the Text widget. Add `text_box.delete(1.0, END)` before inserting.

---

## 🎯 Learning Outcomes
- Successfully created and sized GUI desktop windows using `Tk()`, `title()`, and `geometry()`.
- Displayed styled typography using `Label` with custom `fg` and `bg` hex colors.
- Collected user input with `Entry` and read it using `.get()`.
- Displayed dynamic multi-line results in a `Text` widget using `.insert(END, ...)`.
- Wired user click events to Python logic using `Button(command=...)`.
