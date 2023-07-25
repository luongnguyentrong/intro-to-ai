import pygame
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_nonogram(rows, cols, solution):
    # Initialize pygame
    pygame.init()

    # Constants
    cell_size = 30
    grid_width = cell_size * len(solution[0])
    grid_height = cell_size * len(solution)

    # Calculate window size
    window_width = grid_width + 100
    window_height = grid_height + 100

    # Create the window
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Nonogram Solved State')

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)

        # Draw column clues in vertical format
        x_offset = 20
        y_offset = grid_height + 20
        for col_index, col_clue in enumerate(cols):
            for clue_index, clue in enumerate(col_clue):
                font = pygame.font.Font(None, 24)
                text = font.render(str(clue), True, BLACK)
                screen.blit(text, (x_offset + col_index * cell_size, y_offset + clue_index * cell_size))

        # Draw row clues
        x_offset = grid_width + 20
        y_offset = 20
        for row_index, row_clue in enumerate(rows):
            clue_text = " ".join(str(num) for num in row_clue)
            font = pygame.font.Font(None, 24)
            text = font.render(clue_text, True, BLACK)
            screen.blit(text, (x_offset, y_offset + row_index * cell_size))

        # Draw the nonogram grid
        x_offset = 20
        y_offset = 20
        for row_index, row_data in enumerate(solution):
            for col_index, cell in enumerate(row_data):
                cell_color = BLACK if cell == 1 else WHITE
                pygame.draw.rect(screen, cell_color, (x_offset + col_index * cell_size, y_offset + row_index * cell_size, cell_size, cell_size))

        # Update the display
        pygame.display.update()