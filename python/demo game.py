import pygame


# Initialize Pygame
pygame.init()

# Set the window size and title
screen_width, screen_height = 1720, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Load the player sprite
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set the player starting position
player_rect.centerx = screen_width // 2
player_rect.centery = screen_height // 2

# Set the player movement speed
player_speed = 4

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Update the game state

    # Render the game
    screen.fill((255, 255, 255))
