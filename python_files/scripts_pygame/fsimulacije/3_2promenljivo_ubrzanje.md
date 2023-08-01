## 3_2promenljivo_ubrzanje.py

```python
# Just for fun:
# Telo sa promenljivim ubrzanjem

import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 600
RECT_WIDTH, RECT_HEIGHT = 50, 30

START_X = 100
START_Y = 285
START_SPEED = 0.1

x = START_X
y = START_Y
speed = START_SPEED
acceleration = 0.01

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ubrzanje")
clock = pygame.time.Clock()

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect(speed):
    global x
    x += speed
    if x > WIDTH:
        x = 0
    if x < 0:                   # <---- provera i ako izađe iz levog dela ekrana
        x = WIDTH-RECT_WIDTH

def update_environment(change):
    global speed
    global acceleration
    acceleration += change  # <---- prvi stepen promene: ubrzanje se menja za neku vrednost
    speed += acceleration   # <---- drugi stepen promene: brzina se menja za to novo (promenjeno) ubrzanje

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    update_rect(speed)
    update_environment(-0.00001)
    draw_rect(x, y)

    clock.tick(300)
    pygame.display.update()
```