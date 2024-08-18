import pygame
import random
from settings import *

def create_object(objects, object_type):
    x_pos = random.randint(20, WIDTH - 20)
    y_pos = 0
    rect = pygame.Rect(x_pos, y_pos, 30, 30)
    objects.append(rect)

def update_objects(objects):
    for obj in objects:
        obj.y += OBJECT_SPEED
    objects[:] = [obj for obj in objects if obj.y < HEIGHT]

def check_collisions(player_rect, good_objects, bad_objects, lives, score):
    for obj in good_objects[:]:
        if player_rect.colliderect(obj):
            score += 10
            good_objects.remove(obj)
    for obj in bad_objects[:]:
        if player_rect.colliderect(obj):
            lives -= 1
            bad_objects.remove(obj)
    return lives, score

def save_high_score(score):
    with open("high_scores.txt", "a") as file:
        file.write(f"{score}\n")

def get_high_score():
    try:
        with open("high_scores.txt", "r") as file:
            scores = file.readlines()
            return max(int(score.strip()) for score in scores)
    except ValueError:
        return 0

def draw_text(screen, text, position, font, color=WHITE):
    screen.blit(font.render(text, True, color), position)