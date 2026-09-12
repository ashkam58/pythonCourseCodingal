// ========================================================================
// Prompt Engineering - Lesson 3: Animations with Prompts
// Activity 3: Cat Chaser (Multi-Sprite Interaction)
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/Z71kj3aQbKyZ0Nct_Ug-mGOyvWEKYKt58K8fCUymTZg
// ========================================================================

// ------------------------------------------------------------------------
// Part 1 Prompt:
// "Write Game Lab code to make a cat follow the mouse pointer around the screen."
//
// Part 2 Refined Prompt:
// "Extend the cat code to add a mouse sprite that moves randomly to escape. Keep mouse inside screen bounds."
// ------------------------------------------------------------------------

// Initialize the cat sprite
var cat = createSprite(200, 200);
cat.setAnimation("cat");

// Initialize the fleeing mouse sprite
var mouse = createSprite(100, 100);
mouse.setAnimation("mouse");

function draw() {
  // Clear the screen
  background("lightblue");

  // Cat follows the player's physical mouse pointer
  cat.x = mouseX;
  cat.y = mouseY;

  // The mouse sprite runs randomly to escape
  mouse.x = mouse.x + randomNumber(-3, 3);
  mouse.y = mouse.y + randomNumber(-3, 3);

  // Screen boundary guards: Keep mouse inside the 400x400 canvas
  if (mouse.x < 20) mouse.x = 20;
  if (mouse.x > 380) mouse.x = 380;
  if (mouse.y < 20) mouse.y = 20;
  if (mouse.y > 380) mouse.y = 380;

  // Render both sprites
  drawSprites();
}
