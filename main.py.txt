import pygame
from sound_generator import generate_sound

# Initialize pygame and set up screen
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Adjust as needed
pygame.display.set_caption("RGB Sound Effects")

# Load image
image = pygame.image.load("assets/image.png")
image = pygame.transform.scale(image, (800, 600))  # Scale to fit screen

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position and pixel color
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 0 <= mouse_x < image.get_width() and 0 <= mouse_y < image.get_height():
        color = image.get_at((mouse_x, mouse_y))  # Get RGB at mouse pos
        r, g, b = color[:3]
        
        # Play sound based on RGB values
        generate_sound(r, g, b)
    
    pygame.display.flip()

pygame.quit()
