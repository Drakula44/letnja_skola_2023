# Telo sa promenljivom brzinom - ubrzanje

import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 600
RECT_WIDTH, RECT_HEIGHT = 50, 30

START_X = 100
START_Y = 285
START_SPEED = 0.1 # <--- definisanje početne brzine

x = START_X
y = START_Y
speed = START_SPEED # <--- postavljanje početne brzine

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ubrzanje")
clock = pygame.time.Clock()

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect(speed): 
    global x
    x += speed

def update_environment(change): # <--- funkcija koja će da ažurira okruženje
    global speed
    speed += change # <--- brzina je promenjena za change

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    update_rect(speed)
    update_environment(0.003) # <--- brzina se menja za 0.0005
    draw_rect(x, y)

    clock.tick(300)
    pygame.display.update()