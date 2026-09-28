// ========================================================================
// Prompt Engineering - Lesson 4: Storytelling with Prompts
// After Class Project (ACP): Sea Rescue Adventure
// Platform: Code.org Game Lab (JavaScript)
// Solution Link: https://studio.code.org/projects/gamelab/HnQH6x1_UJSUhU_4BJI3AkF-9N-7AmKJzS-IQbh6vaE
// ========================================================================

// ------------------------------------------------------------------------
// Step 1: Ocean Scene
// Prompt: "Write Game Lab code with an ocean background, a turtle at the bottom, a fish above the water near the top, and a coral reef at the bottom."
//
// Step 2: Turtle Swims Up & Rescues Fish
// Prompt: "Extend the code so the turtle swims upward until it touches the fish, then the fish attaches to the turtle. Add a message showing the rescue."
//
// Step 3: Return & Release Fish
// Prompt: "Extend the code so after rescuing, the turtle swims back down. When it reaches the reef, release the fish so it swims freely using velocity and bounceOff()."
// ------------------------------------------------------------------------

// Underwater background sprite
var bg = createSprite(200, 200);
bg.setAnimation("background_underwater_11_1");

// Hero turtle sprite
var turtle = createSprite(200, 350);
turtle.setAnimation("seaturtle_1");
turtle.scale = 0.3;

// Stranded fish sprite near water surface
var fish = createSprite(200, 50);
fish.setAnimation("fish_pink_1");
fish.scale = 0.8;

// Coral reef sprite at bottom
var reef = createSprite(200, 380);
reef.setAnimation("underseadeco_34_1");
reef.scale = 0.4;

// Story state variables
var rescued = false;
var released = false;
var vx = 0;
var vy = 0;

function draw() {
  background("ocean");

  // State 1: Turtle swims upward to rescue stranded fish
  if (!rescued) {
    fill("white");
    textSize(16);
    text("The turtle swims up to rescue the stranded fish!", 30, 30);
    
    turtle.y -= 2;
    if (turtle.isTouching(fish)) {
      rescued = true;
    }
  }

  // State 2: Fish attaches to turtle; turtle carries it safely down
  else if (!released) {
    fill("white");
    textSize(16);
    text("Fish rescued! Returning to the coral reef...", 50, 30);

    fish.x = turtle.x;
    fish.y = turtle.y - 40; // Fish rests on turtle's back
    turtle.y += 2;          // Carry down

    if (turtle.y >= 300) {
      released = true;
      vx = randomNumber(-3, 3) || 2;
      vy = randomNumber(-3, 3) || -2;
    }
  }

  // State 3: Fish is released and swims freely in the ocean
  else {
    fill("yellow");
    textSize(16);
    text("The fish is safe and swimming freely in the reef! 🐠", 25, 30);

    fish.x += vx;
    fish.y += vy;

    // Edge bouncing
    if (fish.x < 30 || fish.x > 370) vx = -vx;
    if (fish.y < 50 || fish.y > 350) vy = -vy;
  }

  drawSprites();
}
