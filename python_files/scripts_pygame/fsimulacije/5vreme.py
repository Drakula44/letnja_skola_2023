#Vremenski zavisne simulacije

import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 800
RECT_WIDTH, RECT_HEIGHT = 50, 30

START_X = 100
START_Y = 600
SPEED = 0.50

x = START_X
y = START_Y

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linearno kretanje")
clock = pygame.time.Clock()

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect(dt):
    global x
    x += SPEED * dt # <--- vremenski zavisno

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    dt = clock.tick(60) # <--- FPS 60
    update_rect(dt)
    draw_rect(x, y)
    pygame.display.update()