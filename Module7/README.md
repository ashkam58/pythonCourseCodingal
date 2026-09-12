# Module 7: GUI Development with Tkinter

Welcome to **Module 7: GUI Development with Tkinter**! This module covers building complete, interactive graphical desktop applications in Python using Tkinter.

---

## 📚 Lessons Overview

### 🌟 [Lesson 1: Widgets for Starters!](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/)
Introduces Tkinter window creation, the event loop (`mainloop()`), and core widgets (`Label`, `Entry`, `Text`, `Button`).
- [`M7L1A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A1.py): Basic Tkinter window (`Tk()`, `title()`, `geometry()`, `mainloop()`).
- [`M7L1A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A2.py): Getting started with widgets (Name entry, date output, button command).
- [`M7L1ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1ACP.py): Workshop Participant Greeting (Digital welcome desk with `delete(1.0, END)`).

### 📐 [Lesson 2: Tkinter Geometry Managers](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/)
Mastering widget layout and grouping using `Frame`, `relief` borders, `grid()`, `place()`, and password masking with `show="*"`.
- [`M7L2A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A1.py): Number Pad (4x3 keypad matrix using nested loops, `Frame`, `relief=SUNKEN`, and `grid()`).
- [`M7L2A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A2.py): Login App (Registration form with `place()`, password masking with `show="*"`, and personalized text box response).
- [`M7L2ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2ACP.py): ATM PIN Setup Interface (Combines detail frames, SUNKEN outer keypad, RAISED cells, validation, and `place()` layout).

### ⚡ [Lesson 3: Where’s the Event?](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/)
Deep dive into event-driven programming, binding raw keyboard (`<Key>`) and mouse click (`<Button-1>`) events, and displaying dialog alerts with `messagebox`.
- [`M7L3A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A1.py): Event Handler (Binding `<Key>` to print `event.char` and `<Button-1>` to print click events).
- [`M7L3A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A2.py): Virus Detected (`from tkinter import messagebox`, `messagebox.showwarning()`, and button command wiring).
- [`M7L3ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3ACP.py): After-School Routine Checker (Interactive routine tracker with keypress listener, label click listener, and missing task alert popup).

---

## 🔍 In-Depth Technical Concepts

### 1. Geometry Managers Comparison
- **`pack()`**: Stacks widgets vertically or horizontally. Ideal for simple toolbars or top-to-bottom forms.
- **`grid(row=i, column=j)`**: Places widgets in an invisible 2D spreadsheet matrix. Requires `columnconfigure()` and `rowconfigure()` to scale smoothly.
- **`place(x=..., y=...)`**: Pins widgets at exact pixel coordinates relative to parent container. Ideal for fixed-dimension dialogs and forms.
- ⚠️ *Rule of Thumb:* Never mix `grid()` and `pack()` inside the exact same container, as it causes geometry manager deadlocks.

### 2. Event Binding vs. Button Commands
| Feature | `.bind("<Event>", handler)` | `Button(command=handler)` |
|---|---|---|
| **Event Scope** | Universal: Keys, clicks, motion, focus | Click events on that specific button |
| **Handler Parameters** | **Must accept 1 argument:** `def handler(event):` | **Takes 0 arguments:** `def handler():` |
| **Wiring Syntax** | `widget.bind("<Key>", handler)` | `Button(..., command=handler)` |
| **Key Info** | Access typed char via `event.char` | N/A |

### 3. Password Masking
- `Entry(frame, show="*")`: Replaces display characters with `*`.
- Calling `.get()` on the entry **still returns the real unmasked string**!

### 4. Popup Dialogs with `messagebox`
- Must be explicitly imported: `from tkinter import messagebox`
- `messagebox.showwarning(title, message)`: Displays warning dialog and pauses execution until user clicks OK.
- Other variants: `showinfo()`, `showerror()`, `askokcancel()`.

---

## 📂 File Summary

| File | Activity / Project | Key Widgets / Concepts |
|---|---|---|
| [`M7L1A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A1.py) | Activity 1 | `Tk()`, `title()`, `geometry()`, `mainloop()` |
| [`M7L1A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A2.py) | Activity 2 | `Label`, `Entry`, `Button`, `Text`, `date.today()` |
| [`M7L1ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1ACP.py) | ACP Project | Workshop Desk, `delete(1.0, END)`, `insert(END, ...)` |
| [`M7L2A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A1.py) | Activity 1 | `grid()`, nested loops, `Frame`, `relief=SUNKEN` |
| [`M7L2A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A2.py) | Activity 2 | `place()`, `show="*"`, `Frame(master=root)` |
| [`M7L2ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2ACP.py) | ACP Project | ATM PIN Setup, keypad grid, `show="*"`, `confirm_pin()` |
| [`M7L3A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A1.py) | Activity 1 | `.bind("<Key>")`, `event.char`, `.bind("<Button-1>")` |
| [`M7L3A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A2.py) | Activity 2 | `from tkinter import messagebox`, `showwarning()` |
| [`M7L3ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3ACP.py) | ACP Project | After-School Routine Checker, key/mouse events, alerts |
