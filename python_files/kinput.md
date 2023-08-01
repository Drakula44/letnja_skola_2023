## kinput.py

```python
import pygame
import math

pygame.init()

window_size = (800, 800)
SCREEN = pygame.display.set_mode(window_size)
pygame.display.set_caption("Event Demo")

rect1 = pygame.Rect((400-50,400-50),(100,100))

circle_pos = [100, 100]
rad = 30

def draw():
    global circle_pos
    SCREEN.fill("White")
    pygame.draw.circle(SCREEN, "Red", circle_pos, rad)
    pygame.draw.rect(SCREEN,"Red", rect1)
    pygame.display.update()

def racunanje_hip(a: int,b: int) -> int:
    return math.sqrt(math.pow(a,2) + math.pow(b,2)) #c - hipotenuza

clicked1 = False
clicked2 = False
running = True
while running:
    
    draw()
    if clicked1:
        circle_pos = pygame.mouse.get_pos()
    if clicked2:
        rect1.center = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    clicked2 = True
                x1, y2 = circle_pos
                x2, y1 = pygame.mouse.get_pos()
                a = abs(y2 - y1)
                b = abs(x2 - x1)
                if racunanje_hip(a,b) <= rad:
                    clicked1 = True  
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked1 = False
                clicked2 = False


        # elif event.type == pygame.KEYDOWN:
        #     print("Key pressed:", pygame.key.name(event.key))

        # elif event.type == pygame.KEYUP:
        #     print("Key released:", pygame.key.name(event.key))
    pygame.display.update()

pygame.quit()
```