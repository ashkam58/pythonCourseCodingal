# Prompt Engineering - Lesson 4: Storytelling with Prompts

Welcome to **Lesson 4: Storytelling with Prompts**! In this lesson, students learn how to design branching, interactive story games in [Code.org Game Lab](https://studio.code.org/projects/gamelab/new) using progressive prompt engineering.

Students discover how prompts can set up scenes, animate narrative sequences, trigger interactive riddles with clickable choices, and fork into multiple win/lose story endings.

---

## 📚 Overview

### Topics Introduced
1. **Using prompts to set up sprites and scenes**
2. **Sequencing prompts to animate a story flow**
3. **Writing prompts for interactive challenges with multiple choices**
4. **Refining prompts to handle both correct and wrong branching outcomes**

---

## 🔍 Topics in Detail

### 1. Setting Up Sprites & Scenes
Setting up an interactive story starts by describing all characters and backdrops in the prompt:
- *Example Prompt:* `"Create sprites for Earth at the bottom, Friends (girl) in front of Earth, Rocket on the left side, and Astronaut hidden at first."`
- Initializing positions, scales, and visibility (`astronaut.visible = false`) sets the stage before animation begins.

### 2. Sequencing Prompts for Narrative Flow
A story moves through distinct acts or states (`storyStep = 0, 1, 2, ...`):
- **Act 1:** Rocket moves toward the launchpad.
- **Act 2:** Girl boards the rocket and both blast off upward into the sky.
- **Act 3:** Scene switches from Earth (lightblue) to outer space (black with twinkling stars).

### 3. Writing Prompts for Interactive Challenges
Prompts can direct AI to generate interactive decision points:
- Displaying dialogue and riddles: `"I'm full of holes but I can still hold water. What am I?"`
- Generating clickable multiple-choice options (`A) Sponge`, `B) Bucket`, `C) Balloon`) using mouse coordinate boundaries or sprite hitboxes.

### 4. Refining Prompts for Branching Outcomes
Teaching the AI to code consequences based on user choice:
- **Success Branch (Sponge):** Astronaut joins the crew, message shows `"Correct! You freed the astronaut!"`, and they fly back to Earth.
- **Fail Branch (Bucket/Balloon):** Message shows `"Wrong! The astronaut drifts away..."`, background turns warning red, and mission fails.

---

## 🎯 Learning Outcomes
By the end of this lesson, students will:
- Use prompts to configure multi-character story environments.
- Sequence narrative transitions using finite state machines (`storyStep`).
- Create interactive riddles with clickable answer choices.
- Implement conditional branching for victory and defeat outcomes.
- Master sprite coordination (attaching sprites together, e.g. astronaut to rocket).

---

## ⏱️ Lesson Agenda (45–60 mins)

1. **Warm-Up Discussion (5 mins)**:
   - *"How can a story change if you give the computer different instructions?"*
   - Discuss branching storylines like "Choose Your Own Adventure" books.
2. **Activity 1: Space Rescue Story (25 mins)**:
   - Step 1: Make sprites (Earth, Friends, Rocket, Astronaut).
   - Step 2: Rocket takeoff animation.
   - Step 3: Space transition & drifting astronaut.
   - Step 4: Riddle challenge presentation.
   - Step 5 & 6: Success vs. failure branches.
3. **Activity 2: My Prompts Exploration (10 mins)**:
   - Test custom story variations in ChatGPT.
4. **Wrap-Up & Reflection (5 mins)**:
   - Why is exact coordinate/text placement essential for clickable choices?
5. **After Class Project (ACP): Sea Rescue Adventure (15 mins)**:
   - Animate a turtle rescuing a fish, swimming down to a coral reef, and releasing the fish to swim freely.

---

## 📂 Lesson Files & Code

| File | Description |
|---|---|
| [`Activity1_Space_Rescue_Story.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/Activity1_Space_Rescue_Story.js) | Complete Game Lab JavaScript code for Space Rescue Story |
| [`Activity1_Space_Rescue_Story.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/Activity1_Space_Rescue_Story.py) | Interactive Python story engine simulating the branching narrative |
| [`Activity1_Space_Rescue_Story_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/Activity1_Space_Rescue_Story_Solution.md) | Step-by-step teacher guide and activity solution |
| [`ACP_Sea_Rescue_Adventure.js`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/ACP_Sea_Rescue_Adventure.js) | Complete Game Lab JavaScript code for Sea Rescue Adventure |
| [`ACP_Sea_Rescue_Adventure.py`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/ACP_Sea_Rescue_Adventure.py) | Interactive Python simulator for Sea Rescue Adventure |
| [`ACP_Sea_Rescue_Adventure_Solution.md`](file:///c:/Users/ashka/Desktop/pythonCourseCodingal-main/pythonCourseCodingal-main/Prompt%20Engineering/Lesson4_Storytelling_with_Prompts/ACP_Sea_Rescue_Adventure_Solution.md) | Step-by-step ACP solution guide, prompts, and code |

---

## 🔗 Online Resources & Project Links
- [Code.org Game Lab Platform](https://studio.code.org/projects/gamelab/new)
- [Space Rescue Story Completed Game Lab Project](https://studio.code.org/projects/gamelab/qZo0k4VQ2XFfL9WhYj4ct325PRAaWET0yLhCPkVBcNA)
- [ChatGPT Shared Prompts for Space Rescue](https://chatgpt.com/share/68dff719-9dc8-8000-937e-675e7e1f8f15)
- [Sea Rescue Adventure Completed Game Lab Project](https://studio.code.org/projects/gamelab/HnQH6x1_UJSUhU_4BJI3AkF-9N-7AmKJzS-IQbh6vaE)
- [ChatGPT Shared Prompts for Sea Rescue](https://chatgpt.com/share/68dffe3a-7320-8000-9d36-0c3b2b0bb598)
