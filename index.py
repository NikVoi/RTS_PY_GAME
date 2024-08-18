import pygame
import sys
from settings import *
from game_functions import *
from objects import load_player_image

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Go, go, run!")

    player_image, player_rect = load_player_image()

    lives = INITIAL_LIVES
    score = INITIAL_SCORE
    good_objects = []
    bad_objects = []

    font = pygame.font.Font(None, 36)

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += PLAYER_SPEED

        if random.randint(1, 30) == 1:
            create_object(good_objects, 'good')
        if random.randint(1, 50) == 1:
            create_object(bad_objects, 'bad')

        update_objects(good_objects)
        update_objects(bad_objects)

        lives, score = check_collisions(player_rect, good_objects, bad_objects, lives, score)

        for obj in good_objects:
            pygame.draw.rect(screen, WHITE, obj)
        for obj in bad_objects:
            pygame.draw.rect(screen, RED, obj)

        screen.blit(player_image, player_rect)

        draw_text(screen, f"Score: {score}", (10, 10), font)
        draw_text(screen, f"Lives: {lives}", (10, 50), font)

        if lives <= 0:
            save_high_score(score)
            high_score = get_high_score()
            draw_text(screen, "GAME OVER", (WIDTH // 2 - 100, HEIGHT // 2 - 50), font)
            draw_text(screen, f"High Score: {high_score}", (WIDTH // 2 - 120, HEIGHT // 2), font)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()