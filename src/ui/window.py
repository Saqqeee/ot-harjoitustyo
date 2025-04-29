import pygame
from game import Grid


SQUARE_SIZE = 30
MARGIN = 30


class Window:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.grid_width = 10 * SQUARE_SIZE
        self.grid_height = 20 * SQUARE_SIZE

        self.peek_width = 6 * SQUARE_SIZE
        self.peek_height = 5 * SQUARE_SIZE

        window_width = self.grid_width + self.peek_width + 3 * MARGIN
        window_height = self.grid_height + 2 * MARGIN

        self.window = pygame.display.set_mode(
            (window_width, window_height), pygame.RESIZABLE
        )

    def render_frame(self):
        self.window.fill((0, 0, 0))

        self.render_grid()
        self.render_peek()

        pygame.display.flip()

    def render_peek(self):
        offset_left = self.grid_width + 2 * MARGIN

        bounds = pygame.Rect(offset_left, MARGIN, self.peek_width, self.peek_height)
        pygame.draw.rect(self.window, (255, 255, 255), bounds, 1)

        if self.grid.next:
            self.grid.next.spawn(0, 0)

            for square in self.grid.next.squares:
                posx = offset_left + self.peek_width / 3 + SQUARE_SIZE * square.x
                posy = MARGIN + self.peek_height / 3 + SQUARE_SIZE * square.y

                drawable_square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(self.window, square.color, drawable_square, 0)

    def render_grid(self):
        bounds = pygame.Rect(MARGIN, MARGIN, self.grid_width, self.grid_height)
        pygame.draw.rect(self.window, (255, 255, 255), bounds, 1)

        for square in self.grid.squares:
            posx = SQUARE_SIZE * square.x + MARGIN
            posy = SQUARE_SIZE * (square.y - 2) + MARGIN

            drawable_square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

            pygame.draw.rect(self.window, square.color, drawable_square, 0)

        if self.grid.active:
            for square in self.grid.active.squares:
                if square.y < 2:
                    continue
                posx = SQUARE_SIZE * square.x + MARGIN
                posy = SQUARE_SIZE * (square.y - 2) + MARGIN

                drawable_square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(self.window, square.color, drawable_square, 0)
