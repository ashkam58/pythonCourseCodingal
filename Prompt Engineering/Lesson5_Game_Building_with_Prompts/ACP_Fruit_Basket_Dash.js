// ========================================================================
// Prompt Engineering - Lesson 5: Game Building with Prompts
// After Class Project (ACP): Fruit Basket Dash
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/f1nIcO73130b-i7hXnBHi6tXRLtAia7lpYl3XjCGxh4
// ========================================================================

// ------------------------------------------------------------------------
// Step 1: Create background, basket, and fruit sprites
// Step 2: Basket movement with constrain()
// Step 3: Fruit falling and random reset
// Step 4: Catch collision and scoring
// Step 5: 30-second timer and win/lose conditions
// Step 6: Polished HUD bar overlay
// ------------------------------------------------------------------------

// Background sprite
var bg = createSprite(200, 200);
bg.setAnimation("sunshine_showers_1");

// Basket sprite at bottom
var basket = createSprite(200, 350);
basket.setAnimation("bowl_1");

// Falling fruit sprite
var fruit = createSprite(randomNumber(50, 350), 0);
fruit.setAnimation("apple_1_1");
fruit.scale = 0.1;

// Score and timer variables
var score = 0;
var timer = 30;

function draw() {
  background("skyblue");

  if (timer > 0) {
    // 1. Move basket left and right
    if (keyDown("left")) {
      basket.x -= 5;
    }
    if (keyDown("right")) {
      basket.x += 5;
    }

    // Keep basket strictly inside the screen boundaries
    basket.x = constrain(basket.x, 30, 370);

    // 2. Fruit falls down
    fruit.y += 5;

    // 3. Basket catches fruit
    if (fruit.isTouching(basket)) {
      score++;
      fruit.y = 0;
      fruit.x = randomNumber(50, 350);
    }

    // 4. Reset fruit if missed past bottom
    if (fruit.y > 400) {
      fruit.y = 0;
      fruit.x = randomNumber(50, 350);
    }

    // 5. Countdown timer (Game Lab runs at 30 FPS)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Draw all sprites
    drawSprites();

    // 6. HUD (Heads-Up Display) – overlay on top of sprites
    fill("white");
    rect(0, 0, 400, 40);

    fill("black");
    textSize(20);
    text("Score: " + score, 20, 25);
    text("Time: " + timer, 300, 25);
  }

  // End of game screen
  else {
    drawSprites();

    fill("yellow");
    textSize(30);

    if (score >= 10) {
      text("You Win! 🍎", 125, 200);
      textSize(20);
      fill("white");
      text("Apples Caught: " + score, 130, 240);
    } else {
      text("Game Over!", 125, 200);
      textSize(20);
      fill("white");
      text("Apples Caught: " + score + " (Needed 10)", 95, 240);
    }
  }
}
