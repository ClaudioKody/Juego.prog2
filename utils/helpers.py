
import pygame

def load_image(path, scale=1):
    image = pygame.image.load(path).convert_alpha()
    if scale != 1:
        size = image.get_size()
        image = pygame.transform.scale(image, (int(size[0] * scale), int(size[1] * scale)))
    return image

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)
