// ========================================================================
// Prompt Engineering - Lesson 3: Animations with Prompts
// Activity 1: Rocket Builder (Flying into Space)
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/kDN5KqtRPMFvdjF2tjyJUA6b4OrnSQlcg_28nOj2RKk
// ========================================================================

// ------------------------------------------------------------------------
// Prompt to paste into ChatGPT:
// "Write Game Lab code to make a rocket sprite move upward as if it's flying into space."
// ------------------------------------------------------------------------

// Initialize rocket sprite at the lower center of the canvas
var rocket = createSprite(200, 350);
rocket.setAnimation("rocket"); // Make sure "rocket" is added in the Animation tab

function draw() {
  // Clear the screen to a deep space black background
  background("black");

  // Move upward by decreasing the y-coordinate every frame
  rocket.y = rocket.y - 2;

  // Render all active sprites
  drawSprites();
}
