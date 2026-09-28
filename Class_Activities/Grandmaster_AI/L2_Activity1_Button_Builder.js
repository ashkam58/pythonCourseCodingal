// ========================================================================
// Prompt Engineering - Lesson 2: Clear Prompts, Clear Code
// Activity 1: Button Builder (From Words to Code)
// Target Platform: Code.org Game Lab (JavaScript)
// ========================================================================

// ------------------------------------------------------------------------
// Part 1 Code: Background Setup
// Prompt: "You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. Create a draw() loop and set the background to skyblue. No shapes yet."
// ------------------------------------------------------------------------
/*
function draw() {
  background("skyblue");
}
*/

// ------------------------------------------------------------------------
// Part 2 Code: Shapes & Button Layout
// Prompt: "Extend the previous Code.org Game Lab code. Keep the skyblue background. Add a red circle at the top and a yellow rectangle at the bottom with the text 'Click Me'."
// ------------------------------------------------------------------------
/*
function draw() {
  background("skyblue");

  // Red circle at top
  fill("red");
  ellipse(200, 80, 100, 100);

  // Button rectangle
  fill("yellow");
  rect(150, 350, 100, 40);

  // Button text
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);
}
*/

// ------------------------------------------------------------------------
// Part 3 & Complete Full Code: Button Click Interactivity
// Prompt: "Extend the previous Code.org Game Lab code to add click interactivity. Create a hidden sprite centered at (200, 370) sized 100x40 to detect clicks (createSprite + mousePressedOver). Declare a global bgColor defaulting to 'skyblue'. In draw(), call background(bgColor) so the color persists. When the sprite is clicked, update bgColor to a new random color using rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). Keep the red circle at the top and the button visuals and include drawSprites(). Return the full code."
// ------------------------------------------------------------------------

// Hidden button sprite for click detection
var button = createSprite(200, 370, 100, 40);
button.visible = false;

// Background color that persists across frames
var bgColor = "skyblue";

function draw() {
  // Use the persistent background color
  background(bgColor);

  // Red circle at the top
  fill("red");
  ellipse(200, 80, 100, 100);

  // Yellow button visuals near the bottom
  fill("yellow");
  rect(150, 350, 100, 40);

  // Button label
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);

  // Change background color once on click
  if (mousePressedOver(button)) {
    bgColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
  }

  // Draw (hidden) sprites to keep mousePressedOver working
  drawSprites();
}
