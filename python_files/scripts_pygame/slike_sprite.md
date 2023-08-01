## slike_sprite.py

```python
import pygame as pg

image_path = '/home/drakula/projects/letnja_skola_2023/scripts_pygame/assets/p1_stand.png'

image_paths = [
    f"/home/drakula/projects/letnja_skola_2023/scripts_pygame/assets/p1_walk/p1_walk{i:02d}.png"
    for i in range(1, 12)
]

pg.init()
WIDTH = 640
HEIGHT = 480
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Ucitavanje slike
images = [pg.image.load(image_paths[i]) for i in range(len(image_paths))]

# Ucitavanje sprite-a
sprite = pg.sprite.Sprite()
sprite.rect = images[0].get_rect()
sprite.rect.center = (WIDTH // 2, HEIGHT // 2)
print(sprite.rect)

while True:
    for i in range(len(images)):
        screen.fill(pg.Color('black'))
        sprite.image = images[i]
        screen.blit(sprite.image, sprite.rect)
        pg.display.flip()
        pg.time.delay(30)

```