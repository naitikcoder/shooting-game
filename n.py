#1. Target for shooting based on area - 100,50,25,10 outside target is 0
#2. Target keeps oscillating in certain direction- left/right, front/ back
#3. Shooter- mouse pointer and shoot using space
#4. Score- adds on based on the area we hit
#5. Game over/ reset- min 50 score in 5 hits and score 300 in max 8 hits to move to the next leve
import pygame

import random

pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
pygame.display.set_caption('gyfvdjiufvxdhufg')

close = False
x = random.randint(80,110)
y = random.randint(80,100)
colour1 = pygame.Color(132, 90, 89)
colour2 = pygame.Color(255, 0, 255)
colour3 = pygame.Color(255,255,0)
score = 0
direction = +60
directiony = +60
font = pygame.font.Font(None, 20)

font1 = font.render('10',True,[12,23,45])

Font1 = font.render("30",True,[12,23,45])

FOnt1 = font.render('100',True,[12,23,45])




while not close :
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True

        # Type programm here
    screen.fill((12, 45, 80))
    Font2 = font.render(str(score), True, [123, 123, 123])
    screen.blit(Font2, (200, 200))
    win = pygame.font.Font(None, 300)


    if score >=200:
        win = win.render('You won', True, [45, 123, 210])
        screen.blit(win, (200, 450))
    elif score <= -50:
        win = win.render('You lose', True, [45, 123, 210])
        screen.blit(win, (200, 450))
    else:
        if x < 80:
            direction = +40

        elif x > 1100:
            direction = -40
        if y < 80:
            directiony = +40
        elif y > 700:
            directiony = -40
        x = x + direction
        y = y + directiony
        x1, y2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, colour1, (x, y), 140, 140)
        pygame.draw.circle(screen, colour2, (x, y), 100, 100)
        pygame.draw.circle(screen, colour3, (x, y), 60, 60)
        screen.blit(font1, (x + 100, y))
        screen.blit(Font1, (x + 80, y))
        screen.blit(FOnt1, (x + 30, y))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x1, y2, 54, 45))

                if screen.get_at((x1, y2)) == colour1:
                    score = score + 10
                elif screen.get_at((x1, y2)) == colour2:
                    score = score + 30
                elif screen.get_at((x1, y2)) == colour3:
                    score = score + 100
                else:
                    score = score - 10

        pygame.draw.circle(screen, (0, 0, 0), (x1, y2), 100, 10)
        pygame.draw.line(screen, (0, 255, 0), (x1 + 100, y2), (x1 - 100, y2), 10)
        pygame.draw.line(screen, (0, 0, 255), (x1, y2 + 100), (x1, y2 - 100), 10)

    pygame.display.flip()
