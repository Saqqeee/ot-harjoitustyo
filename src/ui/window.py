import pygame
from game import Grid


SQUARE_SIZE = 30
MARGIN = 30


class Window:
    """
    A class for handling rendering. It is essentially
    in charge of everything that's drawn to the screen.

    Attributes:
        grid: The Grid object holding the game state.
    """

    def __init__(self, grid: Grid):
        """
        Constructor of Window.

        Args:
            grid: The Grid object holding the game state.
        """
        self.grid = grid
        self.grid_width = 10 * SQUARE_SIZE
        self.grid_height = 20 * SQUARE_SIZE

        self.peek_width = 6 * SQUARE_SIZE
        self.peek_height = 5 * SQUARE_SIZE

        self.score_width = self.peek_width
        self.score_height = 0  # The method for rendering the score will update this

        window_width = self.grid_width + self.peek_width + 3 * MARGIN
        window_height = self.grid_height + 2 * MARGIN

        self.window = pygame.display.set_mode(
            (window_width, window_height), pygame.RESIZABLE
        )
        pygame.display.set_caption("Tetris")

    def render(self):
        """
        Renders the window and all its elements
        """
        self.window.fill((0, 0, 0))

        self._render_grid()
        self._render_peek()
        self._render_score()
        self._render_controls()
        if self.grid.game_over:
            self._render_game_over()

        pygame.display.flip()

    def _render_peek(self):
        """
        Renders a box that shows the next tetromino in queue.
        """
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

    def _render_score(self):
        """
        Renders the player's current score
        """
        offset_left = self.grid_width + 2 * MARGIN
        offset_top = MARGIN * 2 + self.peek_height

        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"Score: {self.grid.score}", True, (255, 255, 255))

        self.score_height = text.get_height()

        bounds = pygame.Rect(
            offset_left, offset_top, self.score_width, self.score_height
        )
        pygame.draw.rect(self.window, (255, 255, 255), bounds, 1)

        self.window.blit(text, bounds)

    def _render_controls(self):
        """
        Renders a bunch of text to show the player the controls.
        """
        offset_left = self.grid_width + 2 * MARGIN
        offset_top = MARGIN * 3 + self.peek_height + self.score_height

        controls = [
            "\U00002190 / A - Left",
            "\U00002192 / D - Right",
            "\U00002193 / S - Down",
            "\U00002191 / W - Rotate",
            "Space - Drop",
        ]

        font = pygame.font.SysFont("Arial", 25)

        for line in controls:
            text = font.render(line, True, (255, 255, 255))

            self.window.blit(text, (offset_left, offset_top))

            offset_top += 30

    def _render_grid(self):
        """
        Renders the area in which the main Tetris game happens
        and all the squares within it.
        """
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

    def _render_game_over(self):
        """
        Renders the game over screen if needed.
        """

        game_over_font = pygame.font.SysFont("Arial", 50)

        game_over_text = game_over_font.render(
            "Game Over", True, (200, 10, 10), (0, 0, 0)
        )

        left = MARGIN + (self.grid_width - game_over_text.get_width()) / 2
        top = MARGIN + (self.grid_height - game_over_text.get_height()) / 2

        self.window.blit(
            game_over_text,
            (left, top),
        )

        retry_font = pygame.font.SysFont("Arial", 25)
        retry_text = retry_font.render(
            "Press Enter to try again", True, (200, 200, 200), (0, 0, 0)
        )

        self.window.blit(
            retry_text,
            (left, top + game_over_text.get_height()),
        )
