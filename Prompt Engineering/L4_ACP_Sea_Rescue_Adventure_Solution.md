# After Class Project (ACP): Sea Rescue Adventure - Solution & Guide

## 🌊 Project Overview
- **Title:** Sea Rescue Adventure
- **Module:** Prompt Engineering
- **Lesson:** Storytelling with Prompts
- **Platform:** [Code.org Game Lab](https://studio.code.org/projects/gamelab/new)
- **Live Solution Link:** [View Game Lab Project](https://studio.code.org/projects/gamelab/HnQH6x1_UJSUhU_4BJI3AkF-9N-7AmKJzS-IQbh6vaE)
- **ChatGPT Conversation Link:** [View ChatGPT Prompts](https://chatgpt.com/share/68dffe3a-7320-8000-9d36-0c3b2b0bb598)

---

## 🐢 The Story of the Hero Turtle
> *A playful pink fish jumped too high out of the water and got stranded near the surface, unable to dive back down! The brave sea turtle swims upward, catches the fish gently on its shell, carries it back down to the sanctuary of the coral reef, and releases it to swim happily and freely.*

---

## 🛠️ Step-by-Step Prompts & Code Outputs

### Step 1 — Create the Ocean Scene

#### Prompt:
```text
Write Game Lab code with an ocean background, a turtle at the bottom, a fish above the water near the top, and a coral reef at the bottom.
```

#### Expected Code Output:
```javascript
var bg = createSprite(200, 200);
bg.setAnimation("background_underwater_11_1");

var turtle = createSprite(200, 350);
turtle.setAnimation("seaturtle_1");
turtle.scale = 0.3;

var fish = createSprite(200, 50);
fish.setAnimation("fish_pink_1");
fish.scale = 0.8;

var reef = createSprite(200, 380);
reef.setAnimation("underseadeco_34_1");
reef.scale = 0.4;

function draw() {
  background("ocean");
  drawSprites();
}
```

---

### Step 2 — Turtle Swims Up and Rescues the Fish

#### Prompt:
```text
Extend the code so the turtle swims upward until it touches the fish, then the fish attaches to the turtle. Add a message showing the rescue.
```

#### Expected Code Output:
```javascript
var rescued = false;

function draw() {
  background("ocean");

  if (!rescued) {
    turtle.y -= 2; // Swim upward
    if (turtle.isTouching(fish)) {
      rescued = true;
    }
  } else {
    // Fish attaches to turtle
    fish.x = turtle.x;
    fish.y = turtle.y - 40;
  }

  drawSprites();
}
```

---

### Step 3 — Return and Release the Fish (Full Working Project)

#### Prompt:
```text
Extend the code so after rescuing, the turtle swims back down. When it reaches the reef, release the fish so it swims freely using velocity and bouncing off screen boundaries.
```

#### Full Game Lab Code:
```javascript
var bg = createSprite(200, 200);
bg.setAnimation("background_underwater_11_1");

var turtle = createSprite(200, 350);
turtle.setAnimation("seaturtle_1");
turtle.scale = 0.3;

var fish = createSprite(200, 50);
fish.setAnimation("fish_pink_1");
fish.scale = 0.8;

var reef = createSprite(200, 380);
reef.setAnimation("underseadeco_34_1");
reef.scale = 0.4;

var rescued = false;
var released = false;
var vx = 0;
var vy = 0;

function draw() {
  background("ocean");

  // Act 1: Turtle swims up to rescue fish
  if (!rescued) {
    turtle.y -= 2;
    if (turtle.isTouching(fish)) {
      rescued = true;
    }
  }

  // Act 2: Fish carried down to coral reef
  else if (!released) {
    fish.x = turtle.x;
    fish.y = turtle.y - 40;
    turtle.y += 2; // Swim down

    if (turtle.y >= 300) {
      released = true;
      vx = randomNumber(-3, 3) || 2;
      vy = randomNumber(-3, 3) || -2;
    }
  }

  // Act 3: Fish swims freely in the ocean
  else {
    fish.x += vx;
    fish.y += vy;

    // Bounce off edges
    if (fish.x < 30 || fish.x > 370) vx = -vx;
    if (fish.y < 30 || fish.y > 370) vy = -vy;
  }

  drawSprites();
}
```

---

## 💡 Key Computer Science & Prompting Concepts

1. **Sequential State Transitions**:
   - `rescued` and `released` act as flags to advance the story sequentially:
     $$\text{Swimming Up} \xrightarrow{\text{isTouching}} \text{Carrying Down} \xrightarrow{y \ge 300} \text{Free Swimming}$$
2. **Sprite Synchronization (Parenting)**:
   - Setting `fish.x = turtle.x` and `fish.y = turtle.y - 40` keeps the fish locked to the turtle's coordinates without needing complex physics.
3. **Random Swimming Velocity**:
   - `vx = randomNumber(-3, 3)` gives each test of the project unique organic movement.
