# Prompt Engineering - Lesson 6: Prompt-to-Project Showcase (Capstone)

Welcome to the **Capstone Lesson 6: Prompt-to-Project Showcase**! This is the culmination of the Prompt Engineering curriculum where students combine everything they have learned across all previous lessons into their own custom, self-directed game in [Code.org Game Lab](https://studio.code.org/projects/gamelab/new).

Instead of following a rigid template, students select a game theme from an expansive Choice Board, architect their game using structured prompts, iteratively refine mechanics, add scoring and time limits, overlay a custom HUD, and share their completed project.

---

## 📚 Overview

### Topics Introduced
1. **Designing with Prompts** – Thinking and planning before asking (*"What do I want my game to do?"*).
2. **Step-by-Step Prompting** – Decomposing complex game mechanics into modular prompt steps.
3. **Iterative Refinement** – Testing the generated code in Game Lab, debugging issues, and prompting specific improvements.
4. **Creative Freedom** – Customizing sprites, mechanics, sound effects, rules, and win/lose conditions.

---

## 🔍 Topics in Detail

### 1. Designing with Prompts
Students frame their game concept into a cohesive specification before generating code:
- *Example Concept:* *"I want an underwater diver that collects pearls while avoiding jellyfish within 30 seconds."*
- Identifying key sprites (player, collectible, obstacle), control schemes (arrow keys, mouse, gravity jump), and win/lose conditions.

### 2. Step-by-Step Prompting Architecture
Decomposing big ideas into manageable prompt chunks:
$$\text{Step 1: Background \& Sprites} \longrightarrow \text{Step 2: Player Movement} \longrightarrow \text{Step 3: Core Mechanics} \longrightarrow \text{Step 4: Score/Timer} \longrightarrow \text{Step 5: HUD} \longrightarrow \text{Step 6: End Screen}$$

### 3. Iterative Refinement & Debugging
Using conversational prompts to fix bugs:
- *Movement issue:* *"The car drives off the screen. Add constrain(car.x, 30, 370). "*
- *Scoring issue:* *"The score increases too fast when touching a pearl. Reset the pearl to a random position immediately on contact."*

### 4. Creative Freedom & Polish
Encouraging students to add unique flair:
- Adding sound effects: `playSound(...)`.
- Introducing multi-tier scoring or speed progression.
- Designing custom win/loss victory screens.

---

## 🎮 The 7 Capstone Menu Options (Activity 1)

1. **Meteor Dodger 🚀** – Spaceship dodges tumbling meteors and collects energy stars.
2. **Jungle Escape 🐒🌴** – Monkey jumps over rocks and rivers while collecting bananas.
3. **Animal Rescue 🧺🐶** – Basket catches falling pets before time runs out.
4. **Mystery Door Challenge 🚪🔑** – Solve riddles and click the correct key to unlock the magic portal.
5. **Race to the Finish 🏎️🏁** – Race a speedster against AI obstacles to beat the timer.
6. **Underwater Explorer 🤿🪸** – Scuba diver collects pearls while dodging sea creatures.
7. **Sky Jumper ☁️⭐** – Platform jumper leaping cloud to cloud with gravity and jumping physics.

---

## 🎯 Learning Outcomes
By the end of this capstone lesson, students will:
- Independently plan, prompt, build, and debug a complete arcade game in Game Lab.
- Break down complex multi-system games into clear, sequential prompt instructions.
- Apply collision detection, velocity, gravity, boundary constraints, and timers.
- Build interactive user interfaces with HUD text overlays and game state loops.
- Confidently showcase and explain their prompt engineering workflow.

---

## ⏱️ Lesson Agenda (45–60 mins)

1. **Warm-Up & Idea Brainstorming (5 mins)**:
   - *"If you could make any game, what would it be?"*
   - Introduce the 7 project themes on the Choice Board.
2. **Phase 1: Planning with Prompts (10 mins)**:
   - Students select their theme and write out their 4-6 prompt outline.
3. **Phase 2: Building Step by Step (20 mins)**:
   - Step 1: Starter scene & sprites.
   - Step 2: Controls & motion.
   - Step 3: Collision rules & collectibles.
   - Step 4: Scoring, lives, and timer.
   - Step 5: HUD overlay & Win/Lose screens.
4. **Phase 3: Testing & Polish (10 mins)**:
   - Run in Game Lab, debug with refinement prompts, add custom animations.
5. **Phase 4: Showcase & Reflection (10 mins)**:
   - Share project links, celebrate capstone achievements, and discuss lessons learned.

---

## 📂 Lesson Files & Code

| File | Description |
|---|---|
| [`Activity1_Choose_Your_Own_Game.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/Activity1_Choose_Your_Own_Game.js) | Full Game Lab implementation of the capstone project (Meteor Dodger & Underwater Explorer) |
| [`Activity1_Choose_Your_Own_Game.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/Activity1_Choose_Your_Own_Game.py) | Interactive Python showcase launcher & game simulator |
| [`Activity1_Choose_Your_Own_Game_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/Activity1_Choose_Your_Own_Game_Solution.md) | Capstone activity guide, theme outlines, and prompt progressions |
| [`ACP_Choice_Board_Showcase.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/ACP_Choice_Board_Showcase.js) | Complete Game Lab code for all 5 Choice Board themes |
| [`ACP_Choice_Board_Showcase.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/ACP_Choice_Board_Showcase.py) | Interactive multi-game terminal player for all 5 Choice Board themes |
| [`ACP_Choice_Board_Showcase_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson6_Prompt_to_Project_Showcase/ACP_Choice_Board_Showcase_Solution.md) | Complete ACP solution guide with prompt chains and code for each theme |

---

## 🔗 Online Resources & Project Links
- [Code.org Game Lab Platform](https://studio.code.org/projects/gamelab/new/)
- [Codingal Lesson 6 Showcase Overview](https://www.codingal.com/embed/lesson/32e6d5e9-f62d-4b55-9db2-a396887e965b/#overview)
