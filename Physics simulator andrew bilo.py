import pygame

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Physics Simulator")

# Colors
WHITE = (255, 255, 255)
RED = (200, 50, 50)

# Ball properties
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
velocity_y = 0
gravity = 0.5
bounce_factor = -0.7  # Reduces velocity on bounce

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Apply gravity
    velocity_y += gravity
    ball_y += velocity_y

    # Bounce on ground
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        velocity_y *= bounce_factor  # Reverse & reduce speed

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
