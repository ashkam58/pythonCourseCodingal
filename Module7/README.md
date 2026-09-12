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

### 📝 [Lesson 4: Let’s Build a Text Editor](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/)
Building a fully-functional desktop text editor with OS file pickers, reading and writing files from disk, dynamic title updates, and resizable grid layouts.
- [`M7L4A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L4A1.py): My Text Editor (Desktop text editor with `askopenfilename()`, `asksaveasfilename()`, `with open(...)`, `columnconfigure(1, weight=1)`).
- [`M7L4ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L4ACP.py): Letter Writing Application (Dedicated application for drafting, opening, editing, and saving letters with live title updates).

### 🪙 [Lesson 5: Denomination Calculator](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/)
Multi-window architecture using `Toplevel`, PIL image display, nested functions for direct widget scope access, floor division `//` and modulo `%`, and robust `try/except` validation.
- [`M7L5A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5A1.py): Let’s Top a Window (Minimalist two-window application opening a secondary `Toplevel()` window).
- [`M7L5A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5A2.py): Denomination Calculator (Main window with PIL image banner, confirmation popup, and Toplevel calculating counts for 2000, 500, and 100 notes).
- [`M7L5ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5ACP.py): Reading Schedule Planner (Book reading planner calculating complete days and remaining pages using `//`, `%`, and `try/except`).

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
| **Parentheses Trap** | Never add `()`: `handler` not `handler()` | Never add `()`: `command=func` not `func()` |

### 3. Native File Dialogs (`tkinter.filedialog`)
- **Import:** `from tkinter.filedialog import askopenfilename, asksaveasfilename`
- **Cancellation Safety:** If the user cancels the dialog, the function returns an empty string `""` (falsy). Always guard with:
  ```python
  if not filepath:
      return
  ```
- **Text Widget Indexing:**
  - `1.0` denotes **Line 1, Character 0** (Text lines start at 1, characters start at 0).
  - Clear editor before loading: `txt_edit.delete(1.0, END)`
  - Retrieve editor contents: `text = txt_edit.get(1.0, END)`

### 4. Multi-Window Systems with `Toplevel`
- `root = Tk()` creates the single primary window and event loop manager.
- `top = Toplevel(root)` creates an independent secondary window managed by the system Window Manager.
- **Parent Assignment:** Widgets destined for the top window must explicitly set parent `top` (e.g. `Label(top, ...)`). Setting `Label(root, ...)` will place the widget on the main window instead!
- **Nested Functions:** Defining functions inside `topwin()` allows direct variable access (`entry.get()`) without global variables or parameter passing.

### 5. Denomination Math (`//` and `%`)
- **Floor Division (`//`)**: Extracts the whole count of notes fitting into the amount:
  ```python
  note2000 = amount // 2000
  ```
- **Modulo (`%`)**: Leaves only the remainder to be passed to the next denomination:
  ```python
  amount %= 2000
  ```
- Always process denominations in strictly descending order (`2000 -> 500 -> 100`).

---

## 📂 File Summary

| File | Lesson & Type | Key Widgets / Concepts |
|---|---|---|
| [`M7L1A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A1.py) | L1 Activity 1 | `Tk()`, `title()`, `geometry()`, `mainloop()` |
| [`M7L1A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1A2.py) | L1 Activity 2 | `Label`, `Entry`, `Button`, `Text`, `date.today()` |
| [`M7L1ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L1ACP.py) | L1 ACP | Workshop Desk, `delete(1.0, END)`, `insert(END, ...)` |
| [`M7L2A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A1.py) | L2 Activity 1 | `grid()`, nested loops, `Frame`, `relief=SUNKEN` |
| [`M7L2A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2A2.py) | L2 Activity 2 | `place()`, `show="*"`, `Frame(master=root)` |
| [`M7L2ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L2ACP.py) | L2 ACP | ATM PIN Setup, keypad grid, `show="*"`, `confirm_pin()` |
| [`M7L3A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A1.py) | L3 Activity 1 | `.bind("<Key>")`, `event.char`, `.bind("<Button-1>")` |
| [`M7L3A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3A2.py) | L3 Activity 2 | `from tkinter import messagebox`, `showwarning()` |
| [`M7L3ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L3ACP.py) | L3 ACP | After-School Routine Checker, key/mouse events, alerts |
| [`M7L4A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L4A1.py) | L4 Activity 1 | `askopenfilename`, `asksaveasfilename`, `with open`, `grid()` |
| [`M7L4ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L4ACP.py) | L4 ACP | Letter Writing App, text file editing, dynamic title |
| [`M7L5A1.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5A1.py) | L5 Activity 1 | `Toplevel()`, secondary window lifecycle, `.pack()` |
| [`M7L5A2.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5A2.py) | L5 Activity 2 | Denomination Calculator, `PIL`, nested `calculator()`, `//`, `%`, `try/except` |
| [`M7L5ACP.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Module7/M7L5ACP.py) | L5 ACP | Reading Schedule Planner, Toplevel, reading days and pages |
