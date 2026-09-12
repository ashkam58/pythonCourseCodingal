# Prompt Engineering - Lesson 2: Clear Prompts, Clear Code

Welcome to **Lesson 2: Clear Prompts, Clear Code**! In this lesson, students explore how progressive, refined prompts translate directly into clean, working JavaScript code in [Code.org Game Lab](https://studio.code.org/projects/gamelab/new).

Students learn how each iteration of a prompt—**background → shapes → interactivity**—affects the structure and functionality of the generated code. By the end of this lesson, students will have built interactive apps using ChatGPT as their coding assistant.

---

## 📚 Overview

### Topics Introduced
1. **How prompts influence the quality of code**
2. **Breaking down tasks into smaller prompt steps (Decomposition)**
3. **Refining prompts to add details and complexity**
4. **Using prompts to connect multiple steps into a working app**

---

## 🔍 Topics in Detail

### 1. How Prompts Influence the Quality of Code
The clarity of your prompt determines the accuracy of the generated code:
- **General / Vague prompt:** `"Draw something"` → Yields random, unpredictable, or incomplete code.
- **Clear, specific prompt:** `"Draw a red circle at (200, 80) with size 100x100."` → Yields exact, bug-free coordinates and syntax.

### 2. Breaking Down Tasks into Smaller Prompt Steps
Big coding goals become manageable when decomposed into smaller prompt steps:
- **Step 1:** Create and set up a static background canvas.
- **Step 2:** Add shapes, colors, and text labels.
- **Step 3:** Add event detection and interactivity (clicks, color changes).

### 3. Refining Prompts to Add Details and Complexity
Iterative refinement improves code without breaking previous logic:
- *Start:* `"Set the background to skyblue."`
- *Refined:* `"Keep the skyblue background and add a red circle at the top."`
- *Further Refined:* `"Keep the circle, add a yellow rectangle with text 'Click Me'."`

### 4. Connecting Multiple Steps into a Working App
Prompts act like modular building blocks that stack together:
$$\text{Background} \longrightarrow \text{Background + Shapes} \longrightarrow \text{Background + Shapes + Interactivity}$$

---

## 🎯 Learning Outcomes
By the end of this lesson, students will:
- Understand how prompt clarity directly impacts code correctness.
- Break down programming challenges into smaller, sequential prompt steps.
- Practice refining prompts iteratively to introduce variables and event handling.
- Successfully build interactive apps in Code.org Game Lab using ChatGPT.
- Gain confidence communicating technical logic using natural language prompts.

---

## ⏱️ Lesson Agenda (45–60 mins)

1. **Introduction & Warm-Up (5–7 mins)**:
   - Question: *"If you wanted an AI to code for you, how would you explain what you want?"*
   - Discuss why vague prompts fail and how specific coordinates/colors matter.
2. **Activity 1: Button Builder (15–20 mins)**:
   - Part 1: Background prompt (`draw()` loop with `background("skyblue")`).
   - Part 2: Shape prompt (add red circle + yellow button + label).
   - Part 3: Interactivity prompt (hidden sprite, click detection, random `rgb()`).
3. **Activity 2: My Prompts Exploration (10 mins)**:
   - Experiment with variations in ChatGPT and inspect the generated code.
4. **Wrap-Up & Reflection (5 mins)**:
   - Why is step-by-step prompting superior to dumping one massive prompt?
   - What happens when you skip coordinate or variable specifications?
5. **After Class Project (ACP): Click-to-Color Circle (15 mins)**:
   - Apply the 3-step prompt framework to build a clickable magic circle that changes color.

---

## 📂 Lesson Files

| File | Description |
|---|---|
| [`Activity1_Button_Builder.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/Activity1_Button_Builder.js) | Code.org Game Lab JavaScript code for Activity 1 (Parts 1, 2, 3 & Full App) |
| [`Activity1_Button_Builder.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/Activity1_Button_Builder.py) | Interactive Python simulation & Game Lab prompt tester for Activity 1 |
| [`Activity1_Button_Builder_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/Activity1_Button_Builder_Solution.md) | Step-by-step prompts, explanations, and teacher guide for Activity 1 |
| [`ACP_Click_To_Color_Circle.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/ACP_Click_To_Color_Circle.js) | Code.org Game Lab JavaScript code for the ACP assignment |
| [`ACP_Click_To_Color_Circle.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/ACP_Click_To_Color_Circle.py) | Interactive Python visualizer & prompt workflow tool for ACP |
| [`ACP_Click_To_Color_Circle_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson2_Clear_Prompts_Clear_Code/ACP_Click_To_Color_Circle_Solution.md) | Complete solution guide, prompts, troubleshooting, and reflection for ACP |

---

## 🔗 Online Resources & Project Links
- [Code.org Game Lab Platform](https://studio.code.org/projects/gamelab/new/)
- [Button Builder Completed Solution on Game Lab](https://studio.code.org/projects/gamelab/YyFKRuGWaPIuBPvXhOmOihMOGgOgJ1Nheaca21tyI8E)
- [Chat GPT Activity 1 Shared Prompt](https://chatgpt.com/share/68df8e63-6548-8000-bd73-3b846cada54d)
- [ACP Click-to-Color Completed Solution on Game Lab](https://studio.code.org/projects/gamelab/kDN5KqtRPMFvdjF2tjyJULZaeaAvTDnlRYMDzaGdgAQ)
- [Chat GPT ACP Shared Prompt](https://chatgpt.com/share/68df9ce5-ce5c-8000-ad21-76ba51d10983)
