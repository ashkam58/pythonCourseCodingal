# After Class Project (ACP): Choice Board Showcase - Solution & Guide

## 🏆 Project Overview
- **Title:** Prompt-to-Project Showcase — Choice Board
- **Module:** Prompt Engineering (Capstone)
- **Lesson:** Lesson 6: Prompt-to-Project Showcase
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)

---

## 🎨 The 5 Choice Board Themes

Students choose one theme from the choice board and apply the complete 6-step prompt methodology:

```
[Step 1: Pick Theme] ➔ [Step 2: Starter Scene & Sprites] ➔ [Step 3: Core Mechanic]
         ↓
[Step 6: Win/Lose Screen] ↵ [Step 5: HUD Overlay] ↵ [Step 4: Scoring / Lives / Timer]
```

---

## 🛠️ Step-by-Step Prompt Progression by Theme

### Step 1 & 2: Starter Scene & Player Sprites

#### Universal Prompt Pattern:
```text
Write Game Lab code to create the background and main sprites for the [THEME NAME]. Include a draw() with a skyblue background and drawSprites(). Use the animations in the code and scale where shown.
```

- **Theme A (Fruit Catcher):**
  ```javascript
  var bg = createSprite(200, 200); bg.setAnimation("sunshine_showers_1");
  var basket = createSprite(200, 350); basket.setAnimation("bowl_1");
  var fruit = createSprite(randomNumber(40, 360), 0); fruit.setAnimation("apple_1_1"); fruit.scale = 0.12;
  ```

- **Theme B (Traffic Dodge):**
  ```javascript
  var bg = createSprite(200, 200); bg.setAnimation("background_city_1");
  var car = createSprite(200, 340); car.setAnimation("car_red_1"); car.scale = 0.6;
  var cone = createSprite(randomNumber(40, 360), -20); cone.setAnimation("cone_1"); cone.scale = 0.6;
  ```

- **Theme C (Coral Explorer):**
  ```javascript
  var bg = createSprite(200, 200); bg.setAnimation("background_underwater_11_1");
  var diver = createSprite(60, 320); diver.setAnimation("diver_1"); diver.scale = 0.35;
  var pearl = createSprite(randomNumber(40, 360), randomNumber(60, 320)); pearl.setAnimation("pearl_1"); pearl.scale = 0.25;
  ```

- **Theme D (Jungle Runner):**
  ```javascript
  var bg = createSprite(200, 200); bg.setAnimation("background_jungle");
  var runner = createSprite(80, 340); runner.setAnimation("monkey"); runner.scale = 0.35;
  var log = createSprite(420, 350); log.setAnimation("log_1"); log.scale = 0.5;
  ```

- **Theme E (Treasure Door):**
  ```javascript
  var bg = createSprite(200, 200); bg.setAnimation("background_castle_1");
  var door = createSprite(200, 220); door.setAnimation("door_closed_1"); door.scale = 0.7;
  var keyA = createSprite(110, 330); keyA.setAnimation("key_gold_1");
  var keyB = createSprite(200, 330); keyB.setAnimation("key_silver_1");
  var keyC = createSprite(290, 330); keyC.setAnimation("key_copper_1");
  ```

---

### Step 3: Core Mechanics

#### Universal Prompt:
```text
Extend the [THEME NAME] code to add the core mechanic described below.
```

- **Theme A (Fruit Catcher):** Left/right arrows move basket (`basket.x = constrain(basket.x, 30, 370)`), fruit falls (`fruit.y += 5`), resets at bottom.
- **Theme B (Traffic Dodge):** Left/right arrows steer car, cone falls downward (`cone.y += 6`), resets when passing $y > 430$.
- **Theme C (Coral Explorer):** 4-way arrow controls for diver with screen constraints.
- **Theme D (Jungle Runner):** Monkey runs right; spacebar triggers jump with gravity (`runner.velocityY += 0.6`); logs slide left.
- **Theme E (Treasure Door):** Mouse click checks `if (mousePressedOver(keyB))` to unlock `door_open_1`.

---

### Step 4: Scoring, Lives & Timer

#### Prompt:
```text
Add score (or lives), a 30-second timer, and interactions that change score/lives.
```

- **Code:**
  ```javascript
  var score = 0;
  var lives = 3;
  var timer = 30;

  if (World.frameCount % 30 === 0 && timer > 0) {
    timer--;
  }
  ```

---

### Step 5: HUD Overlay

#### Prompt:
```text
Draw a white top bar with black text for Score/Time after drawSprites() so it overlays all sprites.
```

- **Code:**
  ```javascript
  drawSprites();

  fill("white");
  rect(0, 0, 400, 40);

  fill("black");
  textSize(18);
  text("Score: " + score, 20, 25);
  text("Time: " + timer + "s", 300, 25);
  ```

---

### Step 6: Win/Lose End Screen

#### Prompt:
```text
Stop gameplay when timer <= 0 (or lives <= 0 for dodge) and show a win/lose message.
```

- **Code:**
  ```javascript
  if (timer <= 0 || lives <= 0) {
    drawSprites();
    fill("yellow");
    textSize(28);
    var win = (score >= 10) && (lives > 0);
    text(win ? "You Win! 🏆" : "Game Over!", 125, 210);
  }
  ```

---

## 📤 Submission Checklist
- [x] Picked 1 of the 5 Choice Board themes.
- [x] Implemented all 6 progressive prompt stages in Game Lab.
- [x] Included movement controls, collision detection, and score/lives.
- [x] Added a 30-second countdown timer and top HUD bar.
- [x] Tested both winning and losing outcomes.
- [x] Shared project link generated from Game Lab.
