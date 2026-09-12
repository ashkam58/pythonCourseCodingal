# Activity 1: Button Builder (From Words to Code) - Solution & Teacher Guide

## 📌 Activity Overview
- **Title:** BUTTON BUILDER: FROM WORDS TO CODE
- **Lesson:** Clear Prompts, Clear Code
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new/)
- **Live Solution Link:** [View Completed Game Lab Project](https://studio.code.org/projects/gamelab/YyFKRuGWaPIuBPvXhOmOihMOGgOgJ1Nheaca21tyI8E)
- **ChatGPT Shared Prompt:** [View ChatGPT Conversation](https://chatgpt.com/share/68df8e63-6548-8000-bd73-3b846cada54d)

---

## 🎯 The Three-Step Prompting Method

In this activity, students learn that writing one gigantic prompt often causes AI to hallucinate or miss details. Instead, breaking down the application into three progressive steps produces perfect, working Code.org Game Lab code.

```
[Part 1: Background] ➔ [Part 2: Shapes & Labels] ➔ [Part 3: Interactivity (Click Event)]
```

---

## 🛠️ Step-by-Step Instructions & Prompts

### Part 1 — Set a Background

#### The Prompt:
> *"You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. Create a draw() loop and set the background to skyblue. No shapes yet."*

#### Target JavaScript Code:
```javascript
function draw() {
  background("skyblue");
}
```

#### What We Learned:
- Telling AI to act as a *"Code.org Game Lab assistant"* ensures it uses Game Lab-specific functions (like `draw()`, `background()`) rather than standard HTML/DOM JavaScript.
- *"Write only the JavaScript"* keeps the output clean without markdown fluff.

---

### Part 2 — Set Shapes and Labels

#### The Prompt:
> *"Extend the previous Code.org Game Lab code. Keep the skyblue background. Add a red circle at the top and a yellow rectangle at the bottom with the text 'Click Me'."*

#### Target JavaScript Code:
```javascript
function draw() {
  background("skyblue");
  
  // Red circle at top
  fill("red");
  ellipse(200, 80, 100, 100);
  
  // Button rectangle
  fill("yellow");
  rect(150, 350, 100, 40);
  
  // Button text
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);
}
```

#### What We Learned:
- Saying *"Extend the previous Code.org Game Lab code"* instructs the AI to preserve the `draw()` loop and `background("skyblue")` while adding new elements.
- Defining colors (`fill("red")`, `fill("yellow")`) before shapes ensures each element gets its intended color.

---

### Part 3 — Make It Interactive (Change Background Color Once Per Click)

#### The Prompt:
> *"Extend the previous Code.org Game Lab code to add click interactivity. Create a hidden sprite centered at (200, 370) sized 100x40 to detect clicks (createSprite + mousePressedOver). Declare a global bgColor defaulting to 'skyblue'. In draw(), call background(bgColor) so the color persists. When the sprite is clicked, update bgColor to a new random color using rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). Keep the red circle at the top and the button visuals and include drawSprites(). Return the full code."*

---

## 💻 Complete Full Game Lab Code

```javascript
// Hidden button sprite for click detection
var button = createSprite(200, 370, 100, 40);
button.visible = false;

// Background color variable that persists across frames
var bgColor = "skyblue";

function draw() {
  // Use the persistent background color
  background(bgColor);

  // Red circle at the top
  fill("red");
  ellipse(200, 80, 100, 100);

  // Yellow button visuals near the bottom
  fill("yellow");
  rect(150, 350, 100, 40);

  // Button label
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);

  // Change background color once on click
  if (mousePressedOver(button)) {
    bgColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
  }

  // Draw (hidden) sprites to keep mousePressedOver working
  drawSprites();
}
```

---

## 🔍 Alternative Method (Coordinate-Based Click Detection)

If sprites are not used, mouse coordinates can be checked using `mousePressed()` or `mouseWentDown()`:

```javascript
var bgColor = "skyblue";

function draw() {
  background(bgColor);

  // Red circle at the top
  fill("red");
  noStroke();
  ellipse(200, 50, 100, 100);

  // Yellow rectangle at the bottom (button)
  fill("yellow");
  rect(150, 350, 100, 40);

  // Text on the button
  fill("black");
  textSize(16);
  textAlign(CENTER, CENTER);
  text("Click Me", 200, 370);
}

function mousePressed() {
  // Check if click is inside the button bounding box (x: 150-250, y: 350-390)
  if (mouseX >= 150 && mouseX <= 250 && mouseY >= 350 && mouseY <= 390) {
    bgColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
  }
}
```

---

## 💡 Teacher & Student Discussion Points

1. **Why do we need a global `bgColor` variable?**
   - If we put `background(rgb(...))` directly inside `draw()`, the background would randomize 30 times every second (like a disco strobe light!). Storing it in `bgColor` keeps the color constant until a click event triggers a change.
2. **Why use a hidden sprite?**
   - Game Lab's `mousePressedOver(sprite)` is simpler and more reliable than calculating bounding box boundaries with `mouseX` and `mouseY`.
3. **What happens when you skip details in a prompt?**
   - The AI might use HTML buttons or DOM elements (`document.getElementById`) which will crash or not render in Code.org Game Lab!
