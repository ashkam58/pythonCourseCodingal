# Activity 1: Star Catcher (From Words to Game) - Solution & Teacher Guide

## 📌 Activity Overview
- **Title:** STAR CATCHER: FROM WORDS TO GAME
- **Lesson:** Game Building with Prompts
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **Live Completed Project Link:** [View Game Lab Project](https://studio.code.org/projects/gamelab/nspQBSBdFDrJRA0_LxwLEzgdh7rJyiIw6GJO4irzwI4)
- **ChatGPT Conversation Link:** [View ChatGPT Prompts](https://chatgpt.com/share/68e00476-c52c-8000-826a-72be39d2c76c)

---

## 🎮 The 6-Step Prompt Decomposition

```
[Part 1: Sprites & Setup]
       ↓
[Part 2: Basket Movement]
       ↓
[Part 3: Falling Star & Reset]
       ↓
[Part 4: Catching & Score]
       ↓
[Part 5: 30s Timer & Victory Screen]
       ↓
[Part 6: HUD Overlay on Top]
```

---

## 🛠️ Step-by-Step Prompt Progression

### Part 1 — Create Sprites & Basic Draw Loop
- **Prompt:**
  ```text
  Write Game Lab code that creates a background sprite using santa_1, a basket at the bottom using bowl_1, and one falling star using creature_05_1 (scaled to 0.2). Include draw() with a black background and drawSprites().
  ```
- **Code Output:**
  ```javascript
  var bg = createSprite(200, 200);
  bg.setAnimation("santa_1");

  var basket = createSprite(200, 350);
  basket.setAnimation("bowl_1");

  var star = createSprite(randomNumber(50, 350), 0);
  star.setAnimation("creature_05_1");
  star.scale = 0.2;

  function draw() {
    background("black");
    drawSprites();
  }
  ```

---

### Part 2 — Move the Basket (Left/Right)
- **Prompt:**
  ```text
  Extend the previous code. Make the basket move left with the left arrow and right with the right arrow inside draw().
  ```
- **Code Output:**
  ```javascript
  if (keyDown("left")) {
    basket.x -= 5;
  }
  if (keyDown("right")) {
    basket.x += 5;
  }
  ```

---

### Part 3 — Make the Star Fall & Reset
- **Prompt:**
  ```text
  Extend the code. Make the star fall (star.y += 5) and when it goes past the bottom (y > 400), reset it to the top at a random x.
  ```
- **Code Output:**
  ```javascript
  star.y += 5;

  if (star.y > 400) {
    star.y = 0;
    star.x = randomNumber(50, 350);
  }
  ```

---

### Part 4 — Add Scoring on Catch
- **Prompt:**
  ```text
  Add a score variable. When the star touches the basket, increase score by 1 and reset the star to the top at a random x.
  ```
- **Code Output:**
  ```javascript
  var score = 0;

  // Inside draw():
  if (star.isTouching(basket)) {
    score++;
    star.y = 0;
    star.x = randomNumber(50, 350);
  }
  ```

---

### Part 5 — Add a 30-Second Timer & End Screen
- **Prompt:**
  ```text
  Add a timer = 30. Each second (World.frameCount % 30 === 0) decrement the timer while it's above 0. Only let the game run when timer > 0. When time ends, show 'You Win!' if score >= 10, otherwise 'Game Over!'.
  ```
- **Code Output:**
  ```javascript
  var timer = 30;

  // Inside draw():
  if (timer > 0) {
    if (World.frameCount % 30 === 0) {
      timer--;
    }
    // Gameplay logic (movement, falling, catch)
  } else {
    // End screen
    if (score >= 10) {
      text("You Win! 🌟", 120, 200);
    } else {
      text("Game Over!", 120, 200);
    }
  }
  ```

---

### Part 6 — Add a HUD (Score/Time Above Sprites)
- **Prompt:**
  ```text
  Ensure the score and time text are drawn after drawSprites() so they appear above the background sprite. Add a white rectangle bar at the top and draw black text for the HUD.
  ```
- **Code Output:**
  ```javascript
  drawSprites(); // Draw sprites first

  // HUD bar on top
  fill("white");
  rect(0, 0, 400, 40);

  fill("black");
  textSize(20);
  text("Score: " + score, 20, 25);
  text("Time: " + timer, 300, 25);
  ```

---

## 💻 Full Code (Final Complete Game)

```javascript
// Background sprite
var bg = createSprite(200, 200);
bg.setAnimation("santa_1");

// Basket
var basket = createSprite(200, 350);
basket.setAnimation("bowl_1");

// Falling star
var star = createSprite(randomNumber(50, 350), 0);
star.setAnimation("creature_05_1");
star.scale = 0.2;

// Score & timer
var score = 0;
var timer = 30;

function draw() {
  background("black");

  if (timer > 0) {
    // Move basket left/right
    if (keyDown("left")) {
      basket.x -= 5;
    }
    if (keyDown("right")) {
      basket.x += 5;
    }

    // Star falls
    star.y += 5;

    // Basket catches star
    if (star.isTouching(basket)) {
      score++;
      star.y = 0;
      star.x = randomNumber(50, 350);
    }

    // Reset star if missed
    if (star.y > 400) {
      star.y = 0;
      star.x = randomNumber(50, 350);
    }

    // Countdown timer (30 FPS)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Draw all sprites (background, basket, star)
    drawSprites();

    // HUD – draw text above everything
    fill("white");
    rect(0, 0, 400, 40);
    fill("black");
    textSize(20);
    text("Score: " + score, 20, 25);
    text("Time: " + timer, 300, 25);
  } else {
    // Game over screen
    drawSprites();
    fill("yellow");
    textSize(30);
    if (score >= 10) {
      text("You Win! 🌟", 120, 200);
    } else {
      text("Game Over!", 120, 200);
    }
  }
}
```

---

## 🧠 Key Computer Science Insights
1. **Why `World.frameCount % 30 === 0`?**
   - Game Lab runs at 30 frames every second. The modulus operator `% 30` equals 0 exactly once every 30 frames (i.e. every 1 second).
2. **Layering & Draw Order:**
   - Anything drawn **after** `drawSprites()` will always appear on top of sprites. This prevents the large background sprite from hiding the text or UI bar.
