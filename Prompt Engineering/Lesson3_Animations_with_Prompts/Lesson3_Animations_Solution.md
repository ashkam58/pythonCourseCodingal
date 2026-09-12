# Lesson 3: Animations with Prompts - Class Activities & ACP Solutions

## 🚀 Lesson Overview
- **Module:** Prompt Engineering
- **Lesson:** Animations with Prompts
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **ChatGPT Activity Conversation:** [ChatGPT Prompts](https://chatgpt.com/share/68dfa823-4138-8000-931d-b56c183f5471)
- **ChatGPT ACP Conversation:** [ChatGPT ACP Prompts](https://chatgpt.com/share/68dfb0ff-d484-8000-b3f7-e04d8bc157bd)

---

## 🛰️ Activity 1: Rocket Builder (Flying into Space)

### Objective
Animate a rocket sprite moving continuously upward off the top edge of the screen.

### The Prompt to ChatGPT
```text
Write Game Lab code to make a rocket sprite move upward as if it's flying into space.
```

### Generated Game Lab JavaScript Code
```javascript
var rocket = createSprite(200, 350);
rocket.setAnimation("rocket");

function draw() {
  background("black");
  rocket.y = rocket.y - 2; // move upward
  drawSprites();
}
```

### Engineering Insight
- In Game Lab, `(0, 0)` is the **top-left** corner. Decreasing the y-coordinate (`rocket.y = rocket.y - 2`) moves the sprite **upward**.
- If we used `rocket.y = rocket.y + 2`, the rocket would fall downward instead!

---

## 🐧 Activity 2: Penguin Jumper (Jump & Gravity Simulation)

### Objective
Create a jumping character triggered by keyboard events, then refine the prompt to introduce a realistic gravity curve.

### Step-by-Step Prompt Progression

#### Part 1: Basic Jump on Spacebar
- **Prompt:**
  ```text
  Write Game Lab code where a penguin jumps when the spacebar is pressed.
  ```
- **Code Output:**
  ```javascript
  var penguin = createSprite(200, 300);
  penguin.setAnimation("penguin");

  function draw() {
    background("skyblue");
    if (keyDown("space")) {
      penguin.y = penguin.y - 5; // jump up
    }
    drawSprites();
  }
  ```

#### Part 2: Refined Prompt (Adding Gravity & Ground Collision)
- **Prompt:**
  ```text
  Extend the penguin code to add gravity so the penguin lands back down after jumping.
  ```
- **Full Working Code Output:**
  ```javascript
  var penguin = createSprite(200, 300);
  penguin.setAnimation("penguin");

  var velocityY = 0;
  var ground = 350;

  function draw() {
    background("skyblue");

    // Jump impulse when touching ground
    if (keyDown("space") && penguin.y >= ground) {
      velocityY = -10;
    }

    // Apply gravity acceleration
    velocityY = velocityY + 0.5;
    penguin.y = penguin.y + velocityY;

    // Floor collision
    if (penguin.y > ground) {
      penguin.y = ground;
      velocityY = 0;
    }

    drawSprites();
  }
  ```

### Engineering Insight
- Refinement transformed an artificial elevator movement (`penguin.y - 5`) into a real parabolic arc using acceleration:
  $$\text{speed} = \text{speed} + \text{gravity}$$
  $$\text{position} = \text{position} + \text{speed}$$

---

## 🐱🐭 Activity 3: Cat Chaser (Multi-Sprite Interaction)

### Objective
Animate a cat following the user's cursor while a mouse sprite wanders randomly inside the screen boundaries.

### Step-by-Step Prompt Progression

#### Part 1: Cat Follows Mouse Pointer
- **Prompt:**
  ```text
  Write Game Lab code to make a cat follow the mouse pointer around the screen.
  ```
- **Code Output:**
  ```javascript
  var cat = createSprite(200, 200);
  cat.setAnimation("cat");

  function draw() {
    background("lightblue");
    cat.x = mouseX;
    cat.y = mouseY;
    drawSprites();
  }
  ```

#### Part 2: Refined Prompt (Add Escaping Mouse with Boundaries)
- **Prompt:**
  ```text
  Extend the cat code to add a mouse sprite that moves randomly to escape. Keep mouse inside screen bounds.
  ```
- **Full Working Code Output:**
  ```javascript
  var cat = createSprite(200, 200);
  cat.setAnimation("cat");

  var mouse = createSprite(100, 100);
  mouse.setAnimation("mouse");

  function draw() {
    background("lightblue");

    // Cat tracks player mouse
    cat.x = mouseX;
    cat.y = mouseY;

    // Mouse runs erratically using random step offsets
    mouse.x = mouse.x + randomNumber(-3, 3);
    mouse.y = mouse.y + randomNumber(-3, 3);

    // Screen boundaries (keep inside 0 to 400)
    if (mouse.x < 0) mouse.x = 0;
    if (mouse.x > 400) mouse.x = 400;
    if (mouse.y < 0) mouse.y = 0;
    if (mouse.y > 400) mouse.y = 400;

    drawSprites();
  }
  ```

---

## 🏀 After Class Project (ACP): Bouncing Ball

### Objective
Build a ball sprite that moves horizontally and bounces off the screen edges using velocity reversal.

### Step 1: Create a Ball Sprite
- **Prompt:**
  ```text
  Write Game Lab code to create a ball sprite in the center of the screen.
  ```
- **Code:**
  ```javascript
  var ball = createSprite(200, 200);
  ball.setAnimation("ball");

  function draw() {
    background("white");
    drawSprites();
  }
  ```

### Step 2: Make the Ball Move
- **Prompt:**
  ```text
  Extend the code so the ball moves to the right at a steady speed.
  ```
- **Code:**
  ```javascript
  var ball = createSprite(200, 200);
  ball.setAnimation("ball");

  function draw() {
    background("white");
    ball.x = ball.x + 3;
    drawSprites();
  }
  ```

### Step 3: Make the Ball Bounce (Complete Full Solution)
- **Prompt:**
  ```text
  Extend the ball code so it bounces back when it hits the left or right edge of the screen. Use a velocity variable.
  ```
- **Code:**
  ```javascript
  var ball = createSprite(200, 200);
  ball.setAnimation("ball");

  var velocityX = 3;

  function draw() {
    background("white");
    ball.x = ball.x + velocityX;

    // Detect collision with canvas boundaries (0 and 400)
    if (ball.x > 400 || ball.x < 0) {
      velocityX = -velocityX; // Invert speed to reverse direction!
    }

    drawSprites();
  }
  ```

---

## 💡 Student Reflection & Discussion Questions

1. **Why is `velocityX = -velocityX` so powerful?**
   - Multiplying by $-1$ flips the sign. If `velocityX` is $+3$, it becomes $-3$ (moving left). If it is $-3$, it becomes $+3$ (moving right). This single line handles both wall bounces!
2. **Why do we sequence prompts instead of asking for the final game directly?**
   - Writing progressive prompts lets you verify each mechanic (creation ➔ motion ➔ physics ➔ boundaries). If a bug occurs, you know immediately which step caused it.
