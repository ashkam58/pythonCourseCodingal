# After Class Project (ACP): Click-to-Color Circle - Solution & Guide

## 🎯 Assignment Overview
- **Project Title:** Click-to-Color Circle
- **Module:** Prompt Engineering
- **Lesson:** Clear Prompts, Clear Code
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **Completed Project Solution Link:** [View Game Lab Completed Project](https://studio.code.org/projects/gamelab/kDN5KqtRPMFvdjF2tjyJULZaeaAvTDnlRYMDzaGdgAQ)
- **ChatGPT Conversation Link:** [View ChatGPT Prompt Thread](https://chatgpt.com/share/68df9ce5-ce5c-8000-ad21-76ba51d10983)

---

## 🌟 The Magic Toy Story
> *Imagine the circle is a magic glowing orb or jewel! Each time you tap or click on it, it absorbs magical energy and glows with a brand-new vibrant random color. By writing clear, sequential prompts, we teach an AI assistant to build this interactive toy using variables, loops, and mouse event listeners.*

---

## 🛠️ Step-by-Step Procedure & Prompts

### Step 1 — Make a Background

#### Prompt to paste into ChatGPT:
```text
You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. Create a draw() loop and set the background to skyblue. No shapes yet.
```

#### Code Output:
```javascript
function draw() {
  background("skyblue");
}
```

---

### Step 2 — Add an Object (Circle)

#### Prompt to paste into ChatGPT:
```text
Extend the previous Code.org Game Lab code. Keep the skyblue background. Add a red circle at the center using ellipse(200, 200, 100, 100). Return the full code.
```

#### Code Output:
```javascript
function draw() {
  background("skyblue");

  // Red circle at the center
  fill("red");
  ellipse(200, 200, 100, 100);
}
```

---

### Step 3 — Make the Object Change Color on Click

#### Prompt to paste into ChatGPT:
```text
Extend the previous Code.org Game Lab code to make the circle change color when clicked. Create a global variable circleColor defaulting to 'red'. In draw(), call background("skyblue"), then fill(circleColor) and draw ellipse(200, 200, 100, 100). Detect clicks using mouseWentDown() and check if the click is inside the circle with dist(mouseX, mouseY, 200, 200) < 50. When clicked, set circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). Return the full code.
```

---

## 💻 Complete Full Solution Code (Code.org Game Lab)

### Method 1: Using `dist()` to check if click is inside the circle radius (Most Accurate)
```javascript
// Variable to hold the dynamic circle color
var circleColor = "red";

function draw() {
  // Clear screen every frame
  background("skyblue");

  // Draw the magic circle
  fill(circleColor);
  noStroke();
  ellipse(200, 200, 100, 100);

  // Detect left mouse click and verify it happened within radius 50 of center (200, 200)
  if (mouseWentDown("leftButton")) {
    if (dist(mouseX, mouseY, 200, 200) < 50) {
      circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
    }
  }
}
```

### Method 2: Global Click Switch
```javascript
var circleColor = "red";

function draw() {
  background("skyblue");
  
  fill(circleColor);
  ellipse(200, 200, 100, 100);
  
  if (mouseWentDown("leftButton")) {
    circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
  }
}
```

---

## 🧠 Key Technical Concepts Explained

1. **Variables (`var circleColor`)**:
   - Stores the state of the color across multiple frames of the `draw()` loop. Without this variable, the color would not remember its updated state.
2. **`mouseWentDown("leftButton")` vs `mouseDown()`**:
   - `mouseWentDown()` triggers **only once** per click press, which prevents the circle from flickering through 20 different colors during a single click.
3. **`dist(mouseX, mouseY, x, y) < radius`**:
   - Calculates the Euclidean distance from the mouse to the center of the circle. Because the diameter is `100`, the radius is `50`. If the mouse is within `50` units, the click was inside the circle!
4. **`rgb(randomNumber(0, 255), ...)`**:
   - Randomly samples Red, Green, and Blue light values to generate over 16.7 million possible vibrant colors!

---

## 📤 Submission Instructions
1. Open your project on [Code.org Game Lab](https://studio.code.org/projects/gamelab/new).
2. Click the **"Share"** button in the top-left menu bar.
3. Copy your project's unique sharing link.
4. Paste the link into your Codingal ACP submission portal.
