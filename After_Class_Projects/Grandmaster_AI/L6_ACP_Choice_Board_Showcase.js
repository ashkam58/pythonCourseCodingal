// ========================================================================
// Prompt Engineering - Lesson 6: Prompt-to-Project Showcase (Capstone)
// After Class Project (ACP): Choice Board Showcase
// Platform: Code.org Game Lab (JavaScript)
//
// INSTRUCTIONS:
// This file contains complete working solutions for all 5 Choice Board Themes:
// - Theme A: Fruit Catcher
// - Theme B: Traffic Dodge (Active below)
// - Theme C: Coral Explorer
// - Theme D: Jungle Runner
// - Theme E: Treasure Door
// ========================================================================

// ========================================================================
// THEME B: TRAFFIC DODGE (Active Implementation)
// ========================================================================

// Step 1: Background and Sprites
var bg = createSprite(200, 200);
bg.setAnimation("background_city_1");

// Player car
var car = createSprite(200, 340);
car.setAnimation("car_red_1");
car.scale = 0.6;

// Traffic cone hazard
var cone = createSprite(randomNumber(40, 360), -20);
cone.setAnimation("cone_1");
cone.scale = 0.6;

// Game state
var lives = 3;
var score = 0;
var timer = 30;

function draw() {
  background("skyblue");

  if (timer > 0 && lives > 0) {
    // Step 2 & 3: Movement & Hazards
    if (keyDown("left")) car.x -= 5;
    if (keyDown("right")) car.x += 5;
    car.x = constrain(car.x, 30, 370);

    // Hazard falls downward
    cone.y += 6;
    if (cone.y > 430) {
      cone.y = -20;
      cone.x = randomNumber(40, 360);
      score++; // Score increases for successfully dodged cones
    }

    // Step 4: Collision detection
    if (car.isTouching(cone)) {
      lives--;
      cone.y = -20;
      cone.x = randomNumber(40, 360);
    }

    // Timer (30 FPS)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Step 5: Draw sprites and HUD overlay
    drawSprites();

    fill("white");
    rect(0, 0, 400, 40);
    fill("black");
    textSize(18);
    text("Dodged: " + score, 20, 25);
    text("Lives: " + lives, 170, 25);
    text("Time: " + timer + "s", 300, 25);
  } else {
    // Step 6: Win / Lose End Screen
    drawSprites();
    fill("yellow");
    textSize(28);

    if (lives > 0 && timer <= 0) {
      text("You Win! 🏆", 140, 200);
      textSize(18);
      fill("white");
      text("You survived the highway dash!", 90, 240);
    } else {
      text("Game Over! 💥", 125, 200);
      textSize(18);
      fill("white");
      text("Car damaged! Try again!", 115, 240);
    }
  }
}

/*
// ========================================================================
// THEME C: CORAL EXPLORER (Reference Code)
// ========================================================================
var bg = createSprite(200, 200);
bg.setAnimation("background_underwater_11_1");
var diver = createSprite(60, 320);
diver.setAnimation("diver_1");
diver.scale = 0.35;
var pearl = createSprite(randomNumber(40, 360), randomNumber(60, 320));
pearl.setAnimation("pearl_1");
pearl.scale = 0.25;
var score = 0;
var timer = 30;

function drawCoralExplorer() {
  background("skyblue");
  if (timer > 0) {
    if (keyDown("left")) diver.x -= 4;
    if (keyDown("right")) diver.x += 4;
    if (keyDown("up")) diver.y -= 4;
    if (keyDown("down")) diver.y += 4;
    diver.x = constrain(diver.x, 20, 380);
    diver.y = constrain(diver.y, 60, 360);

    if (diver.isTouching(pearl)) {
      score++;
      pearl.x = randomNumber(40, 360);
      pearl.y = randomNumber(60, 320);
    }
    if (World.frameCount % 30 === 0) timer--;
    drawSprites();

    fill("white"); rect(0, 0, 400, 40);
    fill("black"); textSize(18);
    text("Pearls: " + score, 20, 25); text("Time: " + timer, 300, 25);
  } else {
    drawSprites();
    fill("yellow"); textSize(28);
    text(score >= 10 ? "You Win! 🤿" : "Game Over!", 130, 210);
  }
}
*/

/*
// ========================================================================
// THEME D: JUNGLE RUNNER (Reference Code)
// ========================================================================
var bg = createSprite(200, 200);
bg.setAnimation("background_jungle");
var runner = createSprite(80, 340);
runner.setAnimation("monkey");
runner.scale = 0.35;
var log = createSprite(420, 350);
log.setAnimation("log_1");
log.scale = 0.5;
var score = 0;
var lives = 3;
var timer = 30;

function drawJungleRunner() {
  background("skyblue");
  if (timer > 0 && lives > 0) {
    runner.x += 2;
    if (runner.x > 420) { runner.x = -20; score++; }

    if (keyWentDown("space") && runner.y >= 340) {
      runner.velocityY = -10;
    }
    runner.velocityY += 0.6;
    if (runner.y > 340) { runner.y = 340; runner.velocityY = 0; }

    log.x -= 4;
    if (log.x < -20) log.x = 420;

    if (runner.isTouching(log)) {
      lives--;
      log.x = 420;
    }
    if (World.frameCount % 30 === 0) timer--;
    drawSprites();

    fill("white"); rect(0, 0, 400, 40);
    fill("black"); textSize(18);
    text("Score: " + score, 20, 25); text("Lives: " + lives, 170, 25); text("Time: " + timer, 300, 25);
  } else {
    drawSprites();
    fill("yellow"); textSize(28);
    text(lives > 0 ? "Jungle Cleared! 🐒" : "Game Over!", 110, 210);
  }
}
*/

/*
// ========================================================================
// THEME E: TREASURE DOOR (Reference Code)
// ========================================================================
var bg = createSprite(200, 200);
bg.setAnimation("background_castle_1");
var door = createSprite(200, 220);
door.setAnimation("door_closed_1");
door.scale = 0.7;
var keyA = createSprite(110, 330);
keyA.setAnimation("key_gold_1");
var keyB = createSprite(200, 330); // Correct Key!
keyB.setAnimation("key_silver_1");
var keyC = createSprite(290, 330);
keyC.setAnimation("key_copper_1");
var won = false;

function drawTreasureDoor() {
  background("skyblue");
  drawSprites();
  fill("white"); textSize(16);
  text("Click the right key to open the treasure door!", 40, 40);

  if (mouseWentDown("leftButton")) {
    if (mousePressedOver(keyB)) {
      door.setAnimation("door_open_1");
      won = true;
    }
  }
  if (won) {
    fill("yellow"); textSize(26);
    text("Treasure Unlocked! 🗝️✨", 80, 150);
  }
}
*/
