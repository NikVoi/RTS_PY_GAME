import pygame
from settings import *

def load_player_image():
    player_image = pygame.image.load('./assets/player.png').convert_alpha()
    player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    player_rect = player_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 30))
    
    return player_image, player_rect