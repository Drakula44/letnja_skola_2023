## 6hitac_navise.py

```python
import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 800
BALL_RADIUS = 15

START_X = 500
START_Y = 770
START_SPEED = 10

speed = -START_SPEED
x = START_X
y = START_Y

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hitac navise")
clock = pygame.time.Clock()

def draw_ball():
    global x, y
    pygame.draw.circle(window, (255, 0, 0), (x, y), BALL_RADIUS)

def update_ball(dt):
    global y, speed
    y += speed

    if y > HEIGHT-BALL_RADIUS:
        speed *= -0.9
        y = HEIGHT-BALL_RADIUS # Skloni ovo i vidi šta se desi (clipping)

def update_environment(change):
    global speed
    speed += change


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((255, 255, 255))
    
    dt = clock.tick(60) # <--- FPS 60
    
    draw_ball()
    update_ball(dt)
    update_environment(0.2)

    pygame.display.update()
```