import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        # Move ball
        self.ball.rect.x += self.ball.velocity_x
        self.ball.rect.y += self.ball.velocity_y
        
        # --- Paddle collision check ---
        if self.ball.rect.colliderect(self.left_paddle.rect):
            self.ball.rect.left = self.left_paddle.rect.right  # prevent overlap
            self.ball.velocity_x *= -1
        
        elif self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.rect.right = self.right_paddle.rect.left
            self.ball.velocity_x *= -1
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
