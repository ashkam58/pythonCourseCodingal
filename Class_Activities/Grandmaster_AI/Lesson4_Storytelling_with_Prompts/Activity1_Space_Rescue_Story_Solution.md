# Activity 1: Space Rescue Story - Teacher Guide & Complete Solution

## 📌 Activity Overview
- **Title:** Space Rescue Story
- **Lesson:** Storytelling with Prompts
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **Live Completed Solution Link:** [View Game Lab Project](https://studio.code.org/projects/gamelab/qZo0k4VQ2XFfL9WhYj4ct325PRAaWET0yLhCPkVBcNA)
- **ChatGPT Conversation Link:** [View ChatGPT Prompts](https://chatgpt.com/share/68dff719-9dc8-8000-937e-675e7e1f8f15)

---

## 🎬 The Interactive Story Flow

The story is controlled by a state machine variable `storyStep`:
```
Step 0: Rocket rolls to launchpad on Earth
  ↓
Step 1: Maya boards and rocket blasts off upward
  ↓
Step 2: Transition to space; lost astronaut drifts into view
  ↓
Step "question": Riddle challenge with 3 clickable options
  ↙                                                     ↘
Step 3 (Success: Sponge)                  Step "fail" (Wrong: Bucket/Balloon)
  ↓                                                     ↓
Step 4: Rocket flies back to Earth        Screen turns red; astronaut drifts away
  ↓
Step 5: "Mission Complete!" celebration
```

---

## 🛠️ Step-by-Step Prompt Progression

### Step 1 — Make Sprites
- **Prompt:**
  ```text
  You are a Code.org Game Lab assistant. Write JavaScript to set up an interactive story scene:
  - Earth sprite at bottom center (x: 200, y: 400).
  - Friends (girl) sprite standing on Earth (x: 200, y: 300).
  - Rocket sprite on the left (x: 50, y: 350).
  - Astronaut sprite off-screen on the right (x: 400, y: 200), hidden initially (visible = false).
  Create a draw() loop with a lightblue background and call drawSprites().
  ```

### Step 2 — Rocket Launch Prep & Takeoff
- **Prompt:**
  ```text
  Extend the code to animate the launch:
  - Move the rocket rightward toward the middle (x reaches 150).
  - Once there, make both the rocket and the girl fly upward into the sky together.
  - When they reach y < 100, transition to the space scene.
  ```

### Step 3 — Space Scene & Drifting Astronaut
- **Prompt:**
  ```text
  Extend the code to change the scene to outer space:
  - Turn the background black with a helper function drawStars() that draws small white twinkling circles.
  - Make the astronaut visible and drift leftward across space.
  - When the astronaut reaches x < 250, pause the movement and present a riddle challenge.
  ```

### Step 4 — Riddle Challenge
- **Prompt:**
  ```text
  Display a riddle with clickable multiple-choice options:
  - Riddle: "I'm full of holes but I can hold water. What am I?"
  - Option A: Sponge
  - Option B: Bucket
  - Option C: Balloon
  - Detect clicks using mouseWentDown() and checking the mouseY coordinate of each option.
  ```

### Step 5 — Correct Answer (Rescue & Happy Ending)
- **Prompt:**
  ```text
  If Option A (Sponge) is clicked:
  - Show message: "Correct! You freed the astronaut!"
  - Attach the astronaut to the rocket and fly back down toward Earth.
  - Switch the background back to lightblue and display "Mission Complete!".
  ```

### Step 6 — Wrong Answer (Failure Ending)
- **Prompt:**
  ```text
  If Option B (Bucket) or Option C (Balloon) is clicked:
  - Show message: "Wrong! The astronaut drifts away..."
  - Turn the background to red and make the astronaut float away into deep space.
  ```

---

## 💻 Full Code.org Game Lab Code

```javascript
// Sprites Setup
var rocket = createSprite(50, 350);
rocket.setAnimation("sticker_33_1");
rocket.scale = 0.3;

var astronaut = createSprite(400, 200);
astronaut.setAnimation("astronaut_1");
astronaut.visible = false;
astronaut.scale = 0.2;

var friends = createSprite(200, 300);
friends.setAnimation("green_dress_hands_behind_1");
friends.scale = 0.2;

var earth = createSprite(200, 400);
earth.setAnimation("earth_1");
earth.scale = 0.4;

var storyStep = 0;
var timer = 0;
var message = "";

function draw() {
  // Dynamic Background
  if (storyStep < 2) {
    background("lightblue");
  } else if (storyStep === 2 || storyStep === "question") {
    background("black");
    drawStars();
  } else if (storyStep === "fail") {
    background("red");
  } else {
    background("purple");
    drawStars();
  }

  fill("white");
  textSize(16);

  // Step 0: Prepare Launch
  if (storyStep === 0) {
    text("Maya prepared her rocket to rescue a lost astronaut!", 25, 50);
    rocket.x += 1;
    if (rocket.x > 150) {
      storyStep = 1;
      timer = 0;
    }
  }

  // Step 1: Rocket Takes Off
  else if (storyStep === 1) {
    text("The rocket launched into the sky...", 25, 50);
    rocket.y -= 2;
    friends.y = rocket.y;
    friends.x = rocket.x;
    if (rocket.y < 100) {
      storyStep = 2;
      timer = 0;
    }
  }

  // Step 2: Astronaut Found in Deep Space
  else if (storyStep === 2) {
    text("Deep in space, she found the astronaut floating alone!", 25, 50);
    astronaut.visible = true;
    astronaut.x -= 1;
    if (astronaut.x < 250) {
      storyStep = "question";
      timer = 0;
    }
  }

  // Step 2.5: Interactive Riddle Challenge
  else if (storyStep === "question") {
    text("To free the astronaut, answer this riddle:", 25, 50);
    text("I'm full of holes but I can hold water. What am I?", 25, 120);

    fill("yellow");
    text("A) Sponge", 40, 180);
    text("B) Bucket", 40, 220);
    text("C) Balloon", 40, 260);

    if (mouseWentDown("leftButton")) {
      // Option A: Sponge (Correct)
      if (mouseY > 165 && mouseY < 195 && mouseX > 30 && mouseX < 200) {
        message = "Correct! You freed the astronaut!";
        storyStep = 3;
      }
      // Option B: Bucket (Wrong)
      else if (mouseY > 205 && mouseY < 235 && mouseX > 30 && mouseX < 200) {
        message = "Wrong! The astronaut drifts away...";
        storyStep = "fail";
      }
      // Option C: Balloon (Wrong)
      else if (mouseY > 245 && mouseY < 275 && mouseX > 30 && mouseX < 200) {
        message = "Wrong! The astronaut drifts away...";
        storyStep = "fail";
      }
    }
  }

  // Step 3: Rescue
  else if (storyStep === 3) {
    text(message, 25, 50);
    text("She grabbed the astronaut's hand and pulled him inside!", 25, 80);
    astronaut.x = rocket.x;
    astronaut.y = rocket.y;
    timer++;
    if (timer > 80) {
      storyStep = 4;
    }
  }

  // Step 4: Fly Back to Earth
  else if (storyStep === 4) {
    text("Together they flew back to Earth, safe and happy!", 25, 50);
    rocket.y += 2;
    friends.y = rocket.y;
    astronaut.y = rocket.y;
    if (rocket.y > 300) {
      storyStep = 5;
    }
  }

  // Step 5: Safe Ending
  else if (storyStep === 5) {
    background("lightblue");
    text("Mission Complete! Everyone cheered their return! 🎉", 25, 200);
  }

  // Fail Outcome
  else if (storyStep === "fail") {
    fill("white");
    textSize(18);
    text("Oh no! Wrong answer... The astronaut is still lost!", 25, 200);
    astronaut.x += 2;
  }

  drawSprites();
}

function drawStars() {
  for (var i = 0; i < 20; i++) {
    fill("white");
    noStroke();
    ellipse(randomNumber(0, 400), randomNumber(0, 400), 2, 2);
  }
}
```
