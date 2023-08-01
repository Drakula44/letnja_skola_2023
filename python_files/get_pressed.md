## get_pressed.py

```python
import pygame as pg

pg.init()

# Set up the window
window_size = (900, 600)
screen = pg.display.set_mode(window_size)
pg.display.set_caption("Event Demo")
rect=[200, 150, 20, 20]
# Colors
WHITE = (255, 255, 255)
bullets = [] #[[],[]]
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append([rect[0], rect[1]])
                
    tasteri = pg.key.get_pressed()    
    if tasteri[pg.K_a]:
        rect[0] -= 0.5

    if tasteri[pg.K_d]:
        rect[0] += 0.5

    screen.fill(WHITE)
    pg.draw.rect(screen, "Red", rect)

    for bullet in bullets:
        bullet[1] += 0.1
        pg.draw.circle(screen, "black", bullet, 5)
    # Update the screen
    pg.event.pump()
    pg.display.update()

# Quit Pygame properly
pygame.quit()
```