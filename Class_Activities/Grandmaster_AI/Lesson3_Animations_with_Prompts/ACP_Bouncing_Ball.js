// ========================================================================
// Prompt Engineering - Lesson 3: Animations with Prompts
// After Class Project (ACP): Bouncing Ball
// Platform: Code.org Game Lab (JavaScript)
// Solution / ChatGPT Prompt Link: https://chatgpt.com/share/68dfb0ff-d484-8000-b3f7-e04d8bc157bd
// ========================================================================

// ------------------------------------------------------------------------
// Step 1: Create Ball Sprite
// Prompt: "Write Game Lab code to create a ball sprite in the center of the screen."
//
// Step 2: Move Ball
// Prompt: "Extend the code so the ball moves to the right at a steady speed."
//
// Step 3: Bounce Ball
// Prompt: "Extend the ball code so it bounces back when it hits the left or right edge of the screen. Use a velocity variable."
// ------------------------------------------------------------------------

// Create ball sprite at center
var ball = createSprite(200, 200);
ball.setAnimation("ball"); // Add "ball" from the Animation Library

// Velocity variable controlling horizontal speed and direction
var velocityX = 4;

function draw() {
  // Clear the canvas with white or a sports field background
  background("white");

  // Move the ball along the x-axis
  ball.x = ball.x + velocityX;

  // Collision detection with left (0) and right (400) edges
  if (ball.x > 400 || ball.x < 0) {
    // Reverse direction by flipping the sign of velocityX
    velocityX = -velocityX;
  }

  // Draw the animated sprite
  drawSprites();
}
