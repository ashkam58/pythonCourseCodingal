// ========================================================================
// Prompt Engineering - Lesson 5: Game Building with Prompts
// Activity 1: Star Catcher (From Words to Game)
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/nspQBSBdFDrJRA0_LxwLEzgdh7rJyiIw6GJO4irzwI4
// ========================================================================

// ------------------------------------------------------------------------
// Part 1: Background sprite, basket, and falling star
// Part 2: Basket movement with left/right arrow keys
// Part 3: Star falling and resetting at random x
// Part 4: Scoring on catch
// Part 5: 30-second timer and win/lose end screen
// Part 6: HUD overlay drawn on top of all sprites
// ------------------------------------------------------------------------

// Background sprite
var bg = createSprite(200, 200);
bg.setAnimation("santa_1"); // Or starry night background

// Basket sprite at bottom center
var basket = createSprite(200, 350);
basket.setAnimation("bowl_1");

// Falling star sprite starting at random x
var star = createSprite(randomNumber(50, 350), 0);
star.setAnimation("creature_05_1"); // Or yellow star
star.scale = 0.2;

// Score and timer variables
var score = 0;
var timer = 30;

function draw() {
  background("black");

  // Game is active while timer > 0
  if (timer > 0) {
    // 1. Move basket left/right
    if (keyDown("left")) {
      basket.x -= 5;
    }
    if (keyDown("right")) {
      basket.x += 5;
    }

    // Keep basket within canvas boundaries
    if (basket.x < 30) basket.x = 30;
    if (basket.x > 370) basket.x = 370;

    // 2. Star falls downward
    star.y += 5;

    // 3. Basket catches star -> Increase score and reset star
    if (star.isTouching(basket)) {
      score++;
      star.y = 0;
      star.x = randomNumber(50, 350);
    }

    // 4. Reset star if player misses it and it falls past bottom
    if (star.y > 400) {
      star.y = 0;
      star.x = randomNumber(50, 350);
    }

    // 5. Countdown timer (30 frames per second in Game Lab)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Draw all sprites before HUD so HUD sits on top
    drawSprites();

    // 6. HUD (Heads-Up Display) Overlay
    fill("white");
    rect(0, 0, 400, 40); // Top bar background

    fill("black");
    textSize(20);
    text("Score: " + score, 20, 25);
    text("Time: " + timer, 300, 25);
  }

  // Time is up -> Game Over / Victory screen
  else {
    drawSprites();

    fill("yellow");
    textSize(30);

    if (score >= 10) {
      text("You Win! 🌟", 120, 200);
      textSize(20);
      fill("white");
      text("Final Score: " + score, 135, 240);
    } else {
      text("Game Over!", 120, 200);
      textSize(20);
      fill("white");
      text("Final Score: " + score + " (Needed 10)", 95, 240);
    }
  }
}
