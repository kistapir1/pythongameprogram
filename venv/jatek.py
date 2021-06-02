import pygame
from pygame.locals import *
import random



pygame.init()

class Game():

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
    enemyX_change = 0.1
    enemyY_change= 50
    num_of_enemies = 6


    bulletImg=pygame.image.load('laser.png')
    bulletImg=pygame.transform.scale(bulletImg, (9, 25))
    bulletX = playerX
    bulletY = playerY
    bulletY_change = 0



    def player(X,Y):
        screen.blit(playerIMG, (X, Y))

    def enemy(x, y,):
        screen.blit(enemyImg, (x, y))

    def bullet(x, y):
        screen.blit(bulletImg, (x, y))



    running = True
    while running:

        #screen.fill((0, 0, 100))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left pressed")
                    playerX_change = -0.2
                if event.key == pygame.K_RIGHT:
                    print("right pressed")
                    playerX_change = 0.2
                if event.key == pygame.K_UP:
                      print("up pressed")
                      print(bullet(bulletX, bulletY))
                      bulletY_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        enemyX += enemyX_change

        if enemyX <= 0:
            enemyX_change = 0.1
            enemyY += enemyY_change
        elif enemyX >= 770:
            enemyX_change = -0.1
            enemyY += enemyY_change

        bulletY -= bulletY_change
        bulletX += playerX_change

        if bulletX <= 0:
            bulletX = 0
        elif bulletX >= 736:
            bulletX = 736

        if bulletY <= 0:
            bulletY_change = 10
        #elif bulletY >= 800:


        player(playerX, playerY)
        enemy(enemyX, enemyY)
        bullet(bulletX, bulletY)
        pygame.display.update()

pygame.quit()