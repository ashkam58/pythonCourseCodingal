// ========================================================================
// Prompt Engineering - Lesson 2: Clear Prompts, Clear Code
// After Class Project (ACP): Click-to-Color Circle
// Target Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/kDN5KqtRPMFvdjF2tjyJULZaeaAvTDnlRYMDzaGdgAQ
// ========================================================================

// ------------------------------------------------------------------------
// Step 1 Code: Background Setup
// Prompt: "You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. Create a draw() loop and set the background to skyblue. No shapes yet."
// ------------------------------------------------------------------------
/*
function draw() {
  background("skyblue");
}
*/

// ------------------------------------------------------------------------
// Step 2 Code: Add Circle Object
// Prompt: "Extend the previous Code.org Game Lab code. Keep the skyblue background. Add a red circle at the center using ellipse(200, 200, 100, 100). Return the full code."
// ------------------------------------------------------------------------
/*
function draw() {
  background("skyblue");
  fill("red");
  ellipse(200, 200, 100, 100);
}
*/

// ------------------------------------------------------------------------
// Step 3 & Complete Working Code: Interactive Click-to-Color Circle
// Prompt: "Extend the previous Code.org Game Lab code to make the circle change color when clicked. Create a global variable circleColor defaulting to 'red'. In draw(), call background("skyblue"), then fill(circleColor) and draw ellipse(200, 200, 100, 100). Detect clicks using mouseWentDown() and check if the click is inside the circle with dist(mouseX, mouseY, 200, 200) < 50. When clicked, set circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). Return the full code."
// ------------------------------------------------------------------------

// Global variable storing the current circle color
var circleColor = "red";

function draw() {
  // Clear the screen to persistent skyblue background
  background("skyblue");

  // Draw the magic circle with the variable color
  fill(circleColor);
  noStroke();
  ellipse(200, 200, 100, 100);

  // Check if user clicked the left mouse button
  if (mouseWentDown("leftButton")) {
    // Check if the click coordinates fall within radius 50 of the circle center (200, 200)
    if (dist(mouseX, mouseY, 200, 200) < 50) {
      // Update circleColor with a new random RGB color
      circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
    }
  }
}
