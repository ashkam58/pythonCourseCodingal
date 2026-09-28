# Activity 1: Choose Your Own Game - Teacher Guide & Project Blueprints

## 📌 Activity Overview
- **Title:** Choose Your Own Game (Capstone Showcase)
- **Lesson:** Prompt-to-Project Showcase
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)

---

## 🎨 The 7 Project Menu Options

Students choose one of seven game concepts to build using progressive prompt engineering:

| # | Project Theme | Core Mechanics | Player Sprite | Obstacle / Goal |
|---|---|---|---|---|
| **1** | **Meteor Dodger 🚀** | Left/Right dodging + Falling stars | Spaceship | Meteors (damage) & Stars (points) |
| **2** | **Jungle Escape 🐒** | Runner + Spacebar gravity jump | Monkey | Rolling logs & Floating bananas |
| **3** | **Animal Rescue 🧺** | Bottom slider catching falling pets | Basket | Falling puppies & kittens |
| **4** | **Mystery Door Challenge 🚪** | Clickable choice riddle | Adventurer | 3 Key choices & Magic Portal |
| **5** | **Race to the Finish 🏎️** | Vertical/Horizontal lane speeder | Racecar | AI traffic & finish line timer |
| **6** | **Underwater Explorer 🤿** | 4-way arrow key swimming | Scuba Diver | Sharks (avoid) & Pearls (collect) |
| **7** | **Sky Jumper ☁️** | Platform gravity jumping | Hero | Cloud platforms & falling hazards |

---

## 🛠️ Step-by-Step Prompt Blueprints (Meteor Dodger Example)

### Step 1: Background & Sprites Setup
- **Prompt:**
  ```text
  You are a Code.org Game Lab assistant. Write JavaScript to create a space game:
  - Background sprite using "background_space_1" centered at (200, 200).
  - Player spaceship using "retro_ship_1" at bottom center (200, 340), scaled to 0.35.
  - Tumbling meteor obstacle at a random x (40 to 360) and y = -30, scaled to 0.4.
  - Collectible star at random x (40 to 360) and y = -20, scaled to 0.25.
  Include a draw() loop and call drawSprites().
  ```

### Step 2: Controls & Continuous Motion
- **Prompt:**
  ```text
  Extend the code so the spaceship moves left with the left arrow and right with the right arrow. Use constrain() to keep the ship between x: 30 and 370. Make the meteor fall at speed 6 and the star fall at speed 4. If either passes the bottom (y > 420), reset them to the top at a new random x.
  ```

### Step 3: Collision Rules (Points & Damage)
- **Prompt:**
  ```text
  Add variables for score = 0 and lives = 3. When the ship touches the star, increase score by 1 and reset the star to the top. When the ship touches the meteor, decrease lives by 1 and reset the meteor to the top.
  ```

### Step 4: 30-Second Countdown Timer
- **Prompt:**
  ```text
  Add a timer = 30. Decrement the timer once every second using World.frameCount % 30 === 0. Only run gameplay while timer > 0 and lives > 0.
  ```

### Step 5: Polished HUD Overlay
- **Prompt:**
  ```text
  Draw a white rectangle bar across the top (0, 0, 400, 40) after drawSprites(). Add black text displaying Stars (score), Lives, and Time remaining.
  ```

### Step 6: Win/Lose End Screens
- **Prompt:**
  ```text
  When the timer expires or lives run out, stop moving sprites and show an ending screen. If the player survived with lives > 0 and collected at least 8 stars, show "Mission Success! 🚀", otherwise show "Game Over!".
  ```

---

## 💻 Full Code: Underwater Explorer (Blueprint 2)

```javascript
// Background
var bg = createSprite(200, 200);
bg.setAnimation("background_underwater_11_1");

// Player diver
var diver = createSprite(60, 300);
diver.setAnimation("diver_1");
diver.scale = 0.35;

// Collectible pearl
var pearl = createSprite(randomNumber(50, 350), randomNumber(60, 340));
pearl.setAnimation("pearl_1");
pearl.scale = 0.25;

// Shark obstacle
var shark = createSprite(420, 200);
shark.setAnimation("shark_1");
shark.scale = 0.4;

var score = 0;
var lives = 3;
var timer = 30;

function draw() {
  background("darkblue");

  if (timer > 0 && lives > 0) {
    // 4-way arrow controls
    if (keyDown("left")) diver.x -= 4;
    if (keyDown("right")) diver.x += 4;
    if (keyDown("up")) diver.y -= 4;
    if (keyDown("down")) diver.y += 4;
    diver.x = constrain(diver.x, 20, 380);
    diver.y = constrain(diver.y, 60, 360);

    // Shark swims left across screen
    shark.x -= 5;
    if (shark.x < -40) {
      shark.x = 440;
      shark.y = randomNumber(80, 340);
    }

    // Collect pearl
    if (diver.isTouching(pearl)) {
      score++;
      pearl.x = randomNumber(50, 350);
      pearl.y = randomNumber(60, 340);
    }

    // Shark hit
    if (diver.isTouching(shark)) {
      lives--;
      shark.x = 440;
      shark.y = randomNumber(80, 340);
    }

    // Timer
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    drawSprites();

    // Top HUD
    fill("white");
    rect(0, 0, 400, 40);
    fill("black");
    textSize(18);
    text("Pearls: " + score, 20, 25);
    text("Lives: " + lives, 160, 25);
    text("Time: " + timer + "s", 300, 25);
  } else {
    drawSprites();
    fill("yellow");
    textSize(30);
    if (score >= 8 && lives > 0) {
      text("Deep Sea Champion! 🤿", 40, 200);
    } else {
      text("Expedition Ended!", 80, 200);
    }
  }
}
```
