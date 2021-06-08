import math
import random
import pygame


pygame.init()


screen = pygame.display.set_mode([800, 650])

background = pygame.image.load('urhatter.jpg')
pygame.display.set_caption("Galagaxd")
icon = pygame.image.load('game-console.png')
pygame.display.set_icon(icon)

playerIMG = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('ellenfel.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50, 150)
enemyX_change = 0.6
enemyY_change = 50




bulletImg = pygame.image.load('laser.png')
bulletImg = pygame.transform.scale(bulletImg, (9, 25))
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 1
bullet_state="ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def score(x, y):
    score = font.render("Score : " + str(score_value), True, (139, 0, 139))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (139, 0, 139))
    screen.blit(over_text, (200, 250))


def player(x,y):
    screen.blit(playerIMG, (x, y))

def enemy(x, y,):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:


    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left pressed")
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                print("right pressed")
                playerX_change = 0.6
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(1):

        if enemyY > 440:
            for i in range(1):
                enemyY = 2000
            game_over_text()
            break

        enemyX += enemyX_change
        if enemyX <= 0:
            enemyX_change = 0.6
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -0.6
            enemyY += enemyY_change

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        collision = isCollision(enemyX, enemyY, bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX = random.randint(0, 736)
            enemyY = random.randint(0, 0)

        enemy(enemyX, enemyY)

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    score(textX, testY)
    pygame.display.update()

