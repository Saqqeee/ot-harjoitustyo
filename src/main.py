import pygame
from game import Grid
from ui import Window


def main():
    pygame.init()

    clock = pygame.time.Clock()
    counter = 0
    running = True

    grid = Grid()
    window = Window(grid)

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    grid.move(event.key)

        if counter >= 1000:
            counter -= 1000
            grid.tick()

        window.render_frame()

        pygame.display.flip()

        # Tetris doesn't require a lot of frames per second.
        # We'll keep it at 60 for some smoothness.
        counter += clock.tick(60)

    # Exit app after exiting event loop
    pygame.quit()


if __name__ == "__main__":
    main()
