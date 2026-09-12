// ========================================================================
// Prompt Engineering - Lesson 6: Prompt-to-Project Showcase (Capstone)
// Activity 1: Choose Your Own Game — Project 1: Meteor Dodger
// Platform: Code.org Game Lab (JavaScript)
// ========================================================================

// ------------------------------------------------------------------------
// Game Description:
// Pilot your spaceship across deep space! Dodge incoming meteors from above
// while collecting glowing energy stars. Survive for 30 seconds and score
// at least 8 stars to achieve mission victory!
// ------------------------------------------------------------------------

// Background sprite
var bg = createSprite(200, 200);
bg.setAnimation("background_space_1");

// Player spaceship sprite
var ship = createSprite(200, 340);
ship.setAnimation("retro_ship_1");
ship.scale = 0.35;

// Tumbling meteor obstacle
var meteor = createSprite(randomNumber(40, 360), -30);
meteor.setAnimation("meteor_1");
meteor.scale = 0.4;
var meteorSpeed = 6;

// Collectible star
var star = createSprite(randomNumber(40, 360), -20);
star.setAnimation("star_1");
star.scale = 0.25;
var starSpeed = 4;

// Game state variables
var score = 0;
var lives = 3;
var timer = 30;

function draw() {
  background("black");

  // Active gameplay while timer > 0 and lives > 0
  if (timer > 0 && lives > 0) {
    // 1. Player controls (Left / Right with screen boundary constraint)
    if (keyDown("left")) {
      ship.x -= 6;
    }
    if (keyDown("right")) {
      ship.x += 6;
    }
    ship.x = constrain(ship.x, 30, 370);

    // 2. Obstacle movement: Meteor falls
    meteor.y += meteorSpeed;
    if (meteor.y > 430) {
      meteor.y = -30;
      meteor.x = randomNumber(40, 360);
    }

    // 3. Collectible movement: Star falls
    star.y += starSpeed;
    if (star.y > 420) {
      star.y = -20;
      star.x = randomNumber(40, 360);
    }

    // 4. Collision check: Ship catches Star (+1 Score)
    if (ship.isTouching(star)) {
      score++;
      star.y = -20;
      star.x = randomNumber(40, 360);
    }

    // 5. Collision check: Ship hits Meteor (-1 Life)
    if (ship.isTouching(meteor)) {
      lives--;
      meteor.y = -30;
      meteor.x = randomNumber(40, 360);
    }

    // 6. Countdown Timer (30 FPS)
    if (World.frameCount % 30 === 0) {
      timer--;
    }

    // Draw all active sprites
    drawSprites();

    // 7. Polished HUD Overlay
    fill("white");
    rect(0, 0, 400, 40);

    fill("black");
    textSize(18);
    text("Stars: " + score, 20, 25);
    text("Lives: " + lives, 160, 25);
    text("Time: " + timer + "s", 300, 25);
  }

  // End of Game Screens
  else {
    drawSprites();

    fill("yellow");
    textSize(30);

    var isWin = (timer <= 0 && lives > 0 && score >= 8);

    if (isWin) {
      text("Mission Success! 🚀", 70, 200);
      textSize(20);
      fill("white");
      text("You collected " + score + " stars and survived!", 50, 240);
    } else {
      text("Game Over!", 120, 200);
      textSize(20);
      fill("white");
      if (lives <= 0) {
        text("Your ship took too much damage!", 65, 240);
      } else {
        text("Time ran out! Final Score: " + score + " (Needed 8)", 45, 240);
      }
    }
  }
}
