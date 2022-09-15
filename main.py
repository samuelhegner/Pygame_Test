import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Open a new window
screen_height = 500
screen_width = 700

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

run_game = True

clock = pygame.time.Clock()
draw = pygame.draw

while run_game:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run_game = False  # Flag that we are done so we can exit the while loop

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.

    rect_width = screen_width / 6

    for i in range(6):
        draw.rect(screen, GREEN,
                  [i * rect_width, 0, rect_width, screen_height], 0, 1)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

print("Thanks for playing!")
pygame.quit()