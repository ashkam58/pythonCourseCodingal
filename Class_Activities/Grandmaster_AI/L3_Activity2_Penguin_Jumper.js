// ========================================================================
// Prompt Engineering - Lesson 3: Animations with Prompts
// Activity 2: Penguin Jumper
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/Z71kj3aQbKyZ0Nct_Ug-mHylsEEV22vcOFJA2aO-NfY
// ========================================================================

// ------------------------------------------------------------------------
// Part 1 Prompt:
// "Write Game Lab code where a penguin jumps when the spacebar is pressed."
//
// Part 2 Refined Prompt (Adding Gravity):
// "Extend the penguin code to add gravity so the penguin lands back down after jumping."
// ------------------------------------------------------------------------

// Initialize penguin sprite
var penguin = createSprite(200, 300);
penguin.setAnimation("penguin");

// Physics state variables
var velocityY = 0;
var ground = 350;

function draw() {
  // Clear the screen with skyblue
  background("skyblue");

  // Optional: Draw a nice icy ground line
  stroke("white");
  strokeWeight(6);
  line(0, ground + 20, 400, ground + 20);
  noStroke();

  // Trigger jump impulse only when grounded
  if (keyDown("space") && penguin.y >= ground) {
    velocityY = -10; // Negative velocity moves upward in Game Lab
  }

  // Apply gravitational acceleration downward
  velocityY = velocityY + 0.5;
  penguin.y = penguin.y + velocityY;

  // Collision detection with the ground floor
  if (penguin.y > ground) {
    penguin.y = ground;
    velocityY = 0; // Stop falling once on ground
  }

  // Draw the penguin sprite
  drawSprites();
}
