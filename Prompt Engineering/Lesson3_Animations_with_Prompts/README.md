# Prompt Engineering - Lesson 3: Animations with Prompts

Welcome to **Lesson 3: Animations with Prompts**! In this lesson, students discover how sequenced and refined prompts shape animations in [Code.org Game Lab](https://studio.code.org/projects/gamelab/new) across three hands-on classroom activities and an interactive After Class Project (ACP).

---

## 📚 Overview

### Topics Introduced
1. **Sequencing prompts to build animations step by step**
2. **Refining prompts to add new features and physical behaviors (e.g. velocity, gravity)**
3. **Using prompts to connect multiple sprites in one project**
4. **How prompt specificity improves the accuracy and quality of code**

---

## 🔍 Topics in Detail

### 1. Sequencing Prompts to Build Animations
Animation in Game Lab is powered by modifying sprite coordinates (`x` and `y`) inside the continuous `draw()` loop.
- One prompt starts the baseline motion: *"Make a rocket move upward."*
- Subsequent prompts refine speed, boundaries, or orientation.

### 2. Refining Prompts to Add Features & Physics
Taking a basic user action and adding realistic simulation:
- **Baseline Prompt:** *"Make a penguin jump when the spacebar is pressed."*
- **Refined Prompt:** *"Add gravity so the penguin lands back down after jumping."*
- **Result:** Introduces state variables (`velocityY`, `ground`), gravitational acceleration (`velocityY += 0.5`), and floor collisions.

### 3. Using Prompts to Connect Multiple Sprites
Multi-sprite scenes and chase dynamics:
- **Baseline:** *"Make a cat follow the mouse pointer."*
- **Extended:** *"Add a mouse sprite that escapes randomly and stays inside screen bounds."*
- **Result:** Teaches artificial behavior (random walks) and interactive chasing.

### 4. Prompt Specificity = Better Code
Vague prompts result in missing animation setups, broken loops, or misplaced sprites. Precise instructions (sprite names, key names, velocity values, coordinate constraints) guarantee clean, working code.

---

## 🎯 Learning Outcomes
By the end of this lesson, students will:
- Understand how Game Lab animations update coordinates frame-by-frame inside `draw()`.
- Sequence prompts to progress from static sprites to fluid motion.
- Refine prompts to simulate realistic physics including jump impulses and gravity.
- Implement multi-sprite interactions (mouse pointer following + random escape algorithms).
- Program bouncing boundary collisions using velocity inversion (`velocityX = -velocityX`).

---

## ⏱️ Lesson Agenda (45–60 mins)

1. **Warm-Up & Question (5 mins)**:
   - *"If you wanted to make a sprite move, what's the shortest way you could tell an AI to code it?"*
   - Contrast vague prompts vs. specific coordinate increments.
2. **Activity 1: Rocket Builder (10 mins)**:
   - Prompting continuous upward movement (`rocket.y = rocket.y - 2`).
3. **Activity 2: Penguin Jumper (15 mins)**:
   - Part 1: Spacebar jump trigger (`keyDown("space")`).
   - Part 2: Adding gravity and landing boundaries.
4. **Activity 3: Cat Chaser (15 mins)**:
   - Part 1: Cat following mouse cursor (`cat.x = mouseX; cat.y = mouseY;`).
   - Part 2: Mouse sprite escaping with random step offsets.
5. **Wrap-Up & Reflection (5 mins)**:
   - Why do we refine prompts rather than asking for the final game all at once?
6. **After Class Project: Bouncing Ball**:
   - Creating a ball that moves horizontally and bounces off left/right edges using velocity reversal.

---

## 📂 Lesson Files & Code

| File | Description |
|---|---|
| [`Activity1_Rocket_Builder.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/Activity1_Rocket_Builder.js) | Game Lab JavaScript for Activity 1: Flying Rocket |
| [`Activity2_Penguin_Jumper.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/Activity2_Penguin_Jumper.js) | Game Lab JavaScript for Activity 2: Jump & Gravity |
| [`Activity3_Cat_Chaser.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/Activity3_Cat_Chaser.js) | Game Lab JavaScript for Activity 3: Cat & Mouse Chase |
| [`ACP_Bouncing_Ball.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/ACP_Bouncing_Ball.js) | Game Lab JavaScript for ACP: Bouncing Ball with Velocity Reversal |
| [`Lesson3_Animations_Interactive.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/Lesson3_Animations_Interactive.py) | Interactive Python simulator for all animations |
| [`Lesson3_Animations_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson3_Animations_with_Prompts/Lesson3_Animations_Solution.md) | Complete teacher guide, step-by-step prompts, and solution walkthrough |

---

## 🔗 Online Resources & Project Links
- [Code.org Game Lab Platform](https://studio.code.org/projects/gamelab/new)
- [Rocket Builder Solution Project](https://studio.code.org/projects/gamelab/kDN5KqtRPMFvdjF2tjyJUA6b4OrnSQlcg_28nOj2RKk)
- [Penguin Jumper Solution Project](https://studio.code.org/projects/gamelab/Z71kj3aQbKyZ0Nct_Ug-mHylsEEV22vcOFJA2aO-NfY)
- [Cat Chaser Solution Project](https://studio.code.org/projects/gamelab/Z71kj3aQbKyZ0Nct_Ug-mGOyvWEKYKt58K8fCUymTZg)
- [ChatGPT Shared Prompts for Activities](https://chatgpt.com/share/68dfa823-4138-8000-931d-b56c183f5471)
- [ChatGPT Shared Prompts for ACP](https://chatgpt.com/share/68dfb0ff-d484-8000-b3f7-e04d8bc157bd)
