import pygame
from game import Grid


def main():
    pygame.init()

    window = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)

    clock = pygame.time.Clock()
    counter = 0
    running = True

    grid = Grid()

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            grid.left()
                        case pygame.K_RIGHT:
                            grid.right()
                        case pygame.K_DOWN:
                            grid.down()

        # Set a black background
        window.fill((0, 0, 0))

        if counter >= 1000:
            counter -= 1000
            grid.tick()

        grid.render(window)

        pygame.display.flip()

        # Tetris doesn't require a lot of frames per second.
        # We'll keep it at 60 for some smoothness.
        counter += clock.tick(60)

    # Exit app after exiting event loop
    pygame.quit()


if __name__ == "__main__":
    main()
