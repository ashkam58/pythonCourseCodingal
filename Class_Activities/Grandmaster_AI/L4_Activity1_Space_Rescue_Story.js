// ========================================================================
// Prompt Engineering - Lesson 4: Storytelling with Prompts
// Activity 1: Space Rescue Story (Branching Interactive Narrative)
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/qZo0k4VQ2XFfL9WhYj4ct325PRAaWET0yLhCPkVBcNA
// ========================================================================

// ------------------------------------------------------------------------
// Step 1: Sprites Initialization
// Prompt: "Create sprites for Earth at the bottom, Friends (girl) in front of Earth, Rocket on the left side, and Astronaut hidden at first."
// ------------------------------------------------------------------------

// Rocket sprite
var rocket = createSprite(50, 350);
rocket.setAnimation("sticker_33_1"); // Or "rocket" from animation library
rocket.scale = 0.3;

// Astronaut sprite (hidden initially)
var astronaut = createSprite(400, 200);
astronaut.setAnimation("astronaut_1");
astronaut.visible = false;
astronaut.scale = 0.2;

// Girl / Friends sprite
var friends = createSprite(200, 300);
friends.setAnimation("green_dress_hands_behind_1");
friends.scale = 0.2;

// Earth sprite
var earth = createSprite(200, 400);
earth.setAnimation("earth_1");
earth.scale = 0.4;

// Story state controller and variables
var storyStep = 0;
var timer = 0;
var message = "";

// Optional atmospheric sound
// playSound("sound://category_space/Galactic_center_SFX.mp3", true);

function draw() {
  // Background selection based on narrative stage
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

  // Step 0: Rocket prepares and moves toward the launchpad
  if (storyStep === 0) {
    text("Maya prepared her rocket to rescue a lost astronaut!", 25, 50);
    rocket.x += 1;
    if (rocket.x > 150) {
      storyStep = 1;
      timer = 0;
    }
  }

  // Step 1: Rocket and Maya take off into the sky
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

  // Step 2: In outer space, drifting astronaut is discovered
  else if (storyStep === 2) {
    text("Deep in space, she found the astronaut floating alone!", 25, 50);
    astronaut.visible = true;
    astronaut.x -= 1;
    if (astronaut.x < 250) {
      storyStep = "question";
      timer = 0;
    }
  }

  // Step 3 (question): Interactive Riddle Challenge
  else if (storyStep === "question") {
    text("To free the astronaut, answer this riddle:", 25, 50);
    text("I'm full of holes but I can hold water. What am I?", 25, 120);

    // Clickable options
    fill("yellow");
    text("A) Sponge", 40, 180);
    text("B) Bucket", 40, 220);
    text("C) Balloon", 40, 260);

    // Detect player click on options
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

  // Step 3 (Rescue): Pull astronaut aboard
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

  // Step 4: Flying back to Earth
  else if (storyStep === 4) {
    text("Together they flew back to Earth, safe and happy!", 25, 50);
    rocket.y += 2;
    friends.y = rocket.y;
    astronaut.y = rocket.y;
    if (rocket.y > 300) {
      storyStep = 5;
    }
  }

  // Step 5: Successful Mission Ending
  else if (storyStep === 5) {
    background("lightblue");
    text("Mission Complete! Everyone cheered their safe return! 🎉", 25, 200);
  }

  // Fail Ending
  else if (storyStep === "fail") {
    fill("white");
    textSize(18);
    text("Oh no! Wrong answer...", 25, 180);
    text("The astronaut is still lost in deep space! 🌌", 25, 220);
    astronaut.x += 2; // Astronaut drifts away forever
  }

  // Render all active sprites
  drawSprites();
}

// Helper function: generates twinkling stars in the space background
function drawStars() {
  for (var i = 0; i < 20; i++) {
    fill("white");
    noStroke();
    ellipse(randomNumber(0, 400), randomNumber(0, 400), 2, 2);
  }
}
