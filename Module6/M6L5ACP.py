# M6L5ACP: Space Invader Project - Level Up (Audio & Visual Enhancements)
# After Class Project: Space Invader with Background Music, Sound Effects (Laser & Explosion), Score Milestone Animations, and Graceful Audio Fallbacks

import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame & Mixer
pygame.init()
pygame.mixer.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader - Enhanced Edition")
try:
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)
except pygame.error:
    pass

# Load Background with fallback
try:
    background = pygame.image.load('background.png')
except pygame.error:
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((10, 10, 30))

# Audio / Sound Effects with safe fallback
try:
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)  # Loop indefinitely
except pygame.error:
    pass

def play_sound(sound_file):
    try:
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    except pygame.error:
        pass

# Player
try:
    playerImg = pygame.image.load('player.png')
except pygame.error:
    playerImg = pygame.Surface((64, 64), pygame.SRCALPHA)
    pygame.draw.polygon(playerImg, (0, 255, 128), [(32, 0), (0, 64), (64, 64)])

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Multiple Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    try:
        enemyImg.append(pygame.image.load('enemy.png'))
    except pygame.error:
        fallback_enemy = pygame.Surface((64, 64), pygame.SRCALPHA)
        pygame.draw.circle(fallback_enemy, (255, 50, 50), (32, 32), 24)
        enemyImg.append(fallback_enemy)

    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
try:
    bulletImg = pygame.image.load('bullet.png')
except pygame.error:
    bulletImg = pygame.Surface((16, 32), pygame.SRCALPHA)
    pygame.draw.rect(bulletImg, (255, 255, 0), (4, 0, 8, 24))

bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score & Typography
score_value = 0
font = pygame.font.SysFont('Arial', 32, bold=True)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.SysFont('Arial', 64, bold=True)
game_is_over = False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 60, 60))
    pos_x = (SCREEN_WIDTH - over_text.get_width()) // 2
    pos_y = (SCREEN_HEIGHT - over_text.get_height()) // 2
    screen.blit(over_text, (pos_x, pos_y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    play_sound('laser.wav')

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Main Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready" and not game_is_over:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    if not game_is_over:
        # Player Movement
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

        # Enemy Movement & Collision Checks
        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_is_over = True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            # Check Bullet-Enemy Collision
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                play_sound('explosion.wav')
                bulletY = PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
        elif bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
    else:
        game_over_text()

    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
