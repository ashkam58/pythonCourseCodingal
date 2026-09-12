# After Class Project (ACP): Fruit Basket Dash - Solution & Guide

## 🍎 Project Overview
- **Title:** Fruit Basket Dash
- **Module:** Prompt Engineering
- **Lesson:** Game Building with Prompts
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **Live Solution Link:** [View Game Lab Project](https://studio.code.org/projects/gamelab/f1nIcO73130b-i7hXnBHi6tXRLtAia7lpYl3XjCGxh4)
- **ChatGPT Conversation Link:** [View ChatGPT Prompts](https://chatgpt.com/share/68e00786-46f4-8000-9196-a85234727ae0)

---

## 🧺 Game Story
> *It's raining sweet, delicious apples! Players must slide the basket across the sunny garden to catch as many falling apples as possible within 30 seconds. Catch at least 10 apples before time expires to win!*

---

## 🛠️ Step-by-Step Prompt Progression & Code Outputs

### Step 1 — Create Sprites & Background
- **Prompt:**
  ```text
  Write Game Lab code that creates a background (sunshine_showers_1), a basket (bowl_1) at the bottom, and one fruit (apple_1_1, scaled to 0.1). Include draw() with a skyblue background and drawSprites().
  ```
- **Code:**
  ```javascript
  var bg = createSprite(200, 200);
  bg.setAnimation("sunshine_showers_1");

  var basket = createSprite(200, 350);
  basket.setAnimation("bowl_1");

  var fruit = createSprite(randomNumber(50, 350), 0);
  fruit.setAnimation("apple_1_1");
  fruit.scale = 0.1;

  function draw() {
    background("skyblue");
    drawSprites();
  }
  ```

---

### Step 2 — Move the Basket with Constraints
- **Prompt:**
  ```text
  Extend the code so the basket moves left with the left arrow and right with the right arrow. Keep the basket inside the screen using constrain().
  ```
- **Code:**
  ```javascript
  if (keyDown("left")) {
    basket.x -= 5;
  }
  if (keyDown("right")) {
    basket.x += 5;
  }
  basket.x = constrain(basket.x, 30, 370);
  ```

---

### Step 3 — Make the Fruit Fall & Reset
- **Prompt:**
  ```text
  Extend the code so the fruit falls (fruit.y += 5). If it passes the bottom, reset it to the top with a new random x position.
  ```
- **Code:**
  ```javascript
  fruit.y += 5;

  if (fruit.y > 400) {
    fruit.y = 0;
    fruit.x = randomNumber(50, 350);
  }
  ```

---

### Step 4 — Add Scoring on Catch
- **Prompt:**
  ```text
  Add a score variable. When the fruit touches the basket, increase score by 1 and reset the fruit to the top at a random x.
  ```
- **Code:**
  ```javascript
  var score = 0;

  // Inside draw():
  if (fruit.isTouching(basket)) {
    score++;
    fruit.y = 0;
    fruit.x = randomNumber(50, 350);
  }
  ```

---

### Step 5 — Add a Timer & End Screen
- **Prompt:**
  ```text
  Add a timer = 30 seconds. Decrease it each second using World.frameCount % 30 === 0. When timer reaches 0, show 'You Win! 🍎' if score >= 10, else 'Game Over!'.
  ```
- **Code:**
  ```javascript
  var timer = 30;

  if (timer > 0) {
    if (World.frameCount % 30 === 0) {
      timer--;
    }
    // Gameplay logic
  } else {
    // End screen
    if (score >= 10) {
      text("You Win! 🍎", 125, 200);
    } else {
      text("Game Over!", 125, 200);
    }
  }
  ```

---

### Step 6 — Add HUD for Score & Time (Full Working Game)
- **Prompt:**
  ```text
  Extend the code so after drawSprites(), overlay a white rectangle bar at the top with black text showing score and time.
  ```

#### Complete Full Game Lab Code:
```javascript
// Background sprite
var bg = createSprite(200, 200);
bg.setAnimation("sunshine_showers_1");

// Basket
var basket = createSprite(200, 350);
basket.setAnimation("bowl_1");

// Falling fruit
var fruit = createSprite(randomNumber(50, 350), 0);
fruit.setAnimation("apple_1_1");
fruit.scale = 0.1;

// Score & timer
var score = 0;
var timer = 30;

function draw() {
  background("skyblue");

  if (timer > 0) {
    // Move basket left/right
    if (keyDown("left")) {
      basket.x -= 5;
    }
    if (keyDown("right")) {
      basket.x += 5;
    }
    basket.x = constrain(basket.x, 30, 370);

    // Fruit falls
    fruit.y += 5;

    // Basket catches fruit
    if (fruit.isTouching(basket)) {
      score++;
      fruit.y = 0;
      fruit.x = randomNumber(50, 350);
    }

    // Reset fruit if missed
    if (fruit.y > 400) {
      fruit.y = 0;
      fruit.x = randomNumber(50, 350);
    }

    // Countdown timer (30 FPS)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Draw sprites
    drawSprites();

    // HUD – overlay on top
    fill("white");
    rect(0, 0, 400, 40);
    fill("black");
    textSize(20);
    text("Score: " + score, 20, 25);
    text("Time: " + timer, 300, 25);
  } else {
    // End screen
    drawSprites();
    fill("yellow");
    textSize(30);
    if (score >= 10) {
      text("You Win! 🍎", 125, 200);
    } else {
      text("Game Over!", 125, 200);
    }
  }
}
```

---

## 📤 Submission Checklist
- [x] Background, basket, and fruit sprites render properly.
- [x] Left and right arrow keys control basket smoothly with `constrain()`.
- [x] Apples fall from top and randomize x upon catch or reset.
- [x] Score increments upon basket touch.
- [x] Timer counts down from 30 seconds.
- [x] Top HUD overlay clearly displays Score and Time.
- [x] Win / Lose ending displays correctly when timer expires.
- [x] Shared Game Lab project link submitted on the Codingal platform.
