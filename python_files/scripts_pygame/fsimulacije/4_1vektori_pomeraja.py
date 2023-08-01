# Vektori pomeraja (1/3)

import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 600
RECT_WIDTH, RECT_HEIGHT = 50, 30

START_X = 100
START_Y = 285
SPEED = 0.1

x = START_X
y = START_Y
x_vec = SPEED
y_vec = SPEED


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linearno kretanje")

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect():
    global x, y, x_vec, y_vec
    x += x_vec
    y += y_vec

def update_environment():
    global x_vec, y_vec
    pass

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    update_rect()
    update_environment()
    draw_rect(x, y)

    pygame.display.update()