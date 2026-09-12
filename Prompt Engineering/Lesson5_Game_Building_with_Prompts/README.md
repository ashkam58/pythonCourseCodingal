# Prompt Engineering - Lesson 5: Game Building with Prompts

Welcome to **Lesson 5: Game Building with Prompts**! In this lesson, students learn how to build complete, arcade-style video games in [Code.org Game Lab](https://studio.code.org/projects/gamelab/new) by refining concise prompts step by step.

Students discover how prompts can incrementally construct game entities, user input handling, collision physics, scoring mechanisms, countdown timers, HUD overlays, and win/lose victory screens.

---

## 📚 Overview

### Topics Introduced
1. **Using prompts to create sprites and a basic draw loop**
2. **Refining prompts to add player movement and falling object mechanics**
3. **Writing prompts for scoring rules and entity resets**
4. **Sequencing prompts to build a countdown timer and win/lose conditions**
5. **Improving prompts to add a polished HUD (Heads-Up Display) on top of gameplay**

---

## 🔍 Topics in Detail

### 1. Sprite Initialization & Setup
Setting up the visual canvas and base actors:
- *Example Prompt:* `"Write Game Lab code that creates a background sprite using santa_1, a basket at the bottom using bowl_1, and one falling star using creature_05_1 (scaled to 0.2). Include draw() with a black background and drawSprites()."`
- Establishes dimensions, animations, and coordinates.

### 2. Player Movement & Physics Mechanics
Giving characters responsive controls and continuous motion:
- Arrow key detection: `if (keyDown("left")) basket.x -= 5;`
- Falling objects: `star.y += 5;`
- Screen boundary wrapping: Resetting when $y > 400$ to $y = 0$ with `randomNumber(50, 350)`.

### 3. Scoring Rules & Object Resets
Translating gameplay rules into condition checks:
- Detecting basket collision: `if (star.isTouching(basket))`
- Incremental scoring: `score++;`
- Immediate star repositioning to prevent multi-scoring bugs on a single catch.

### 4. Countdown Timers & Game Over Screens
Introducing urgency and terminal win/lose states:
- Frame rate timing: Using `World.frameCount % 30 === 0` to count down exactly 1 second (Game Lab runs at 30 frames per second).
- Condition checks: When `timer <= 0`, evaluate `if (score >= 10)` to render either **"You Win!"** or **"Game Over!"**.

### 5. Layered HUD (Heads-Up Display)
Ensuring user interface elements render clearly:
- **Draw Order Rule:** Calling `rect()` and `text()` for score and time **after** `drawSprites()` so the background sprite doesn't paint over the text.
- Top white bar with contrasting black text.

---

## 🎯 Learning Outcomes
By the end of this lesson, students will:
- Build a full arcade game from scratch using iterative prompt decomposition.
- Understand Game Lab frame timing (`World.frameCount % 30 === 0`).
- Master object reuse through reset loops (`star.y = 0; star.x = randomNumber(...)`).
- Implement user interface layering with Heads-Up Displays (HUD).
- Configure win/lose state branching based on quantitative gameplay targets.

---

## ⏱️ Lesson Agenda (45–60 mins)

1. **Warm-Up Discussion (5 mins)**:
   - *"What is the minimum instruction you could give to make a computer start a game?"*
   - Discuss how starting with just sprites allows safe, bug-free incremental building.
2. **Activity 1: Star Catcher (30 mins)**:
   - Part 1: Sprites & Draw Loop.
   - Part 2: Basket left/right movement.
   - Part 3: Star falling and boundary reset.
   - Part 4: Collision detection & scoring.
   - Part 5: 30-second timer & end screen.
   - Part 6: HUD overlay on top of sprites.
3. **Activity 2: My Prompts Exploration (5 mins)**:
   - Test custom variations (changing speed, time, target score) in ChatGPT.
4. **Wrap-Up & Reflection (5 mins)**:
   - Why do we draw the HUD after `drawSprites()`?
5. **After Class Project (ACP): Fruit Basket Dash (15 mins)**:
   - Build a sunny fruit catching game with constrained basket movement and falling apples.

---

## 📂 Lesson Files & Code

| File | Description |
|---|---|
| [`Activity1_Star_Catcher.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/Activity1_Star_Catcher.js) | Complete Game Lab JavaScript code for Star Catcher (Parts 1–6) |
| [`Activity1_Star_Catcher.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/Activity1_Star_Catcher.py) | Interactive Python arcade simulator for Star Catcher |
| [`Activity1_Star_Catcher_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/Activity1_Star_Catcher_Solution.md) | Step-by-step teacher guide and prompt progression for Activity 1 |
| [`ACP_Fruit_Basket_Dash.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/ACP_Fruit_Basket_Dash.js) | Complete Game Lab JavaScript code for Fruit Basket Dash |
| [`ACP_Fruit_Basket_Dash.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/ACP_Fruit_Basket_Dash.py) | Interactive Python simulator for Fruit Basket Dash |
| [`ACP_Fruit_Basket_Dash_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson5_Game_Building_with_Prompts/ACP_Fruit_Basket_Dash_Solution.md) | Full ACP project solution, prompts, and code |

---

## 🔗 Online Resources & Project Links
- [Code.org Game Lab Platform](https://studio.code.org/projects/gamelab/new)
- [Star Catcher Completed Game Lab Project](https://studio.code.org/projects/gamelab/nspQBSBdFDrJRA0_LxwLEzgdh7rJyiIw6GJO4irzwI4)
- [ChatGPT Shared Prompts for Star Catcher](https://chatgpt.com/share/68e00476-c52c-8000-826a-72be39d2c76c)
- [Fruit Basket Dash Completed Game Lab Project](https://studio.code.org/projects/gamelab/f1nIcO73130b-i7hXnBHi6tXRLtAia7lpYl3XjCGxh4)
- [ChatGPT Shared Prompts for Fruit Basket Dash](https://chatgpt.com/share/68e00786-46f4-8000-9196-a85234727ae0)
