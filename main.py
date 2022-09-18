# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import random
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 500))
running = True
background=pygame.image.load('background.png')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Shooting')
my_ship = pygame.image.load('space-ship.png')
bullet = pygame.image.load('bullet.png')
enemy = pygame.image.load('enemy.png')
blast=pygame.image.load('blast.png')
my_shipx = 370
my_shipy = 400
bx = my_shipx + 17
by = my_shipy + 18
j = 0
i = 0
kills = 0
scr = "score:"
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, (100, 0, 0), (0, 200, 200))
score = font.render(scr + str(kills), True, (0, 0, 0), (100, 150, 100))
textRect = text.get_rect()
textRect.center = (400, 250)
status = "run"
bulletstate = "shooting"
enemyimg= [None]*5
enemyx= [None]*5
enemyy= [None]*5
changex= [None]*5
changey= [None]*5
n=5
for i in range(0,n):
    enemyimg[i]=pygame.image.load("enemy.png")
    enemyx[i]=random.randint(0, 734)
    enemyy[i]=random.randint(1, 100)
    changex[i]=4
    changex[i]=4
def enemies(enemy,a,b):
    if status == "run":
        screen.blit(enemy, (a, b))


def shoot(a, b):
    if status == "run":
        screen.blit(bullet, (a, b))
        if b==my_shipy+8:
            lxSound = mixer.Sound("laser.wav")
            lxSound.play()

def play(a, b):
    if status == "run":
        screen.blit(my_ship, (a, b))
def blasting(a,b):
    screen.blit(blast, (a,b))

def iscollison(a,b):
    if int(b-5) <= int(by) <=int(b+5) and int(a - 30) <= int(bx) <= int(a + 50):
        return True
    else:
        return False
def game_over():
    global status
    screen.blit(text, textRect)
    status = "Over"

while running:
    x = 0
    s = 0.05
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    keys = pygame.key.get_pressed()
    screen.blit(background,(0,0))
    if keys[pygame.K_LEFT]:
        x = -4
    if keys[pygame.K_RIGHT]:
        x = 4
    my_shipx += x
    if my_shipx < 0:
        my_shipx = 0
    if my_shipx > 736:
        my_shipx = 736
    score = font.render(scr + str(kills), True, (0, 0, 0), (100, 150, 0))
    if keys[pygame.K_SPACE]:
        j = -10
    by+=j
    if by <= 0:
        by = my_shipy
    if by == my_shipy:
        bx = my_shipx + 17
    if(bulletstate=="shooting"):
        shoot(bx, by)
        shoot(bx - 17, by + 18)
        shoot(bx + 17, by + 18)
    else:
        bx=my_shipx
        by=my_shipy
        shoot(bx, by)
        shoot(bx - 17, by + 18)
        shoot(bx + 17, by + 18)
        bulletstate = "shooting"
    play(my_shipx, my_shipy)
    for i in range(n):
        enemies(enemyimg[i],enemyx[i],enemyy[i])
        collison=iscollison(enemyx[i],enemyy[i])
        if collison:
            blasting(enemyx[i],enemyy[i])
            exSound = mixer.Sound("explosion.wav")
            exSound.play()
            bulletstate = "collide"
            kills+=1
            enemyx[i] = random.randint(0, 734)
            enemyy[i] = random.randint(1, 100)
        else:
            changey[i]=0.1*(int((kills+1)/10)+3)
            enemyy[i]+=changey[i]
        if enemyy[i] >=400:
            game_over()
    screen.blit(score, (350, 0))
    pygame.display.update()
