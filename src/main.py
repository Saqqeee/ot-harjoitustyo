import pygame

SQUARE_SIZE = 30

class Grid:
    def __init__(self):
        # We make the underlying grid logic 2 squares taller than what we present to
        # account for new shapes that take up 3 squares vertically
        self.grid = [[0 for _ in range(22)] for _ in range(10)]

        # List of cells on the grid corresponding to the currently active (falling) shape
        self.active: list[tuple] = list()

    def spawn_square(self): # TODO: More shapes and colors
        x = 5
        y = 0

        self.grid[x][y] = 1
        self.grid[x+1][y] = 1
        self.grid[x+1][y+1] = 1
        self.grid[x][y+1] = 1

        self.active = [(x, y), (x+1, y), (x+1, y+1), (x, y+1)]

    def down(self): # TODO: Out of bounds and collision checking
        # Clear the old positions
        for x, y in self.active:
            self.grid[x][y] = 0

        # Fill the new positions
        for i in range(len(self.active)):
            x, y = self.active[i]
            y += 1
            self.grid[x][y] = 1
            self.active[i] = (x, y)


    def render(self, window, margin_left, margin_top):
        bounds = pygame.Rect(margin_left, margin_top, SQUARE_SIZE * 10, SQUARE_SIZE * 20)
        pygame.draw.rect(window, (255, 255, 255), bounds, 1)

        print(self.grid)

        for x in range(10):
            for y in range(2, 22):
                if self.grid[x][y] > 0:
                    posx = SQUARE_SIZE * x + margin_left
                    posy = SQUARE_SIZE * (y - 2) + margin_top

                    square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

                    pygame.draw.rect(window, (255, 0, 0), square, 0)


def main():
    pygame.init()

    window = pygame.display.set_mode((1600, 900))

    clock = pygame.time.Clock()
    counter = 0
    running = True

    grid = Grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Set a black background
        window.fill((0, 0, 0))

        if len(grid.active) == 0:
            grid.spawn_square()

        if counter >= 1000:
            counter -= 1000
            grid.down()

        grid.render(window, SQUARE_SIZE, SQUARE_SIZE)

        pygame.display.flip()

        # Tetris doesn't require a lot of frames per second.
        # We'll keep it at 60 for some smoothness.
        counter += clock.tick(60)

    # Exit app after exiting event loop
    pygame.quit()


if __name__ == "__main__":
    main()