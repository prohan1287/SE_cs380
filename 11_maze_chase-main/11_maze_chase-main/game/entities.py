import pygame
from game.maze import CELL


SPEED = 2


class Player:

    def __init__(self, r, c):

        self.r = r
        self.c = c

        cx = c * CELL + CELL // 2
        cy = r * CELL + CELL // 2

        self.rect = pygame.Rect(
            cx - 12,
            cy - 12,
            24,
            24
        )

        self.color = (0, 100, 255)

    # ---------------------------------------------------------
    # PLAYER MOVEMENT
    # ---------------------------------------------------------

    def move(self, keys, walls, rows, cols):

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = SPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = SPEED

        # Horizontal movement
        new_rect = self.rect.move(dx, 0)

        if self._valid(
            new_rect,
            walls,
            rows,
            cols
        ):
            self.rect = new_rect

        # Vertical movement
        new_rect = self.rect.move(0, dy)

        if self._valid(
            new_rect,
            walls,
            rows,
            cols
        ):
            self.rect = new_rect

    # ---------------------------------------------------------
    # CHECK VALID PLAYER POSITION
    # ---------------------------------------------------------

    def _valid(self, rect, walls, rows, cols):

        for px, py in [
            (rect.left, rect.top),
            (rect.right - 1, rect.top),
            (rect.left, rect.bottom - 1),
            (rect.right - 1, rect.bottom - 1)
        ]:

            cr = py // CELL
            cc = px // CELL

            if not (
                0 <= cr < rows
                and 0 <= cc < cols
            ):
                return False

        return True

    # ---------------------------------------------------------
    # DRAW PLAYER
    # ---------------------------------------------------------

    def draw(self, screen):

        # Blue player
        pygame.draw.circle(
            screen,
            self.color,
            self.rect.center,
            12
        )

        # Small white highlight
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                self.rect.centerx - 4,
                self.rect.centery - 4
            ),
            3
        )


# =============================================================
# ENEMY
# =============================================================

class Enemy:

    def __init__(
        self,
        r,
        c,
        color=(220, 60, 60)
    ):

        self.r = r
        self.c = c

        cx = c * CELL + CELL // 2
        cy = r * CELL + CELL // 2

        self.rect = pygame.Rect(
            cx - 12,
            cy - 12,
            24,
            24
        )

        self.color = color

        # Movement timer
        self.timer = 0

        # Initial movement speed
        self.move_interval = 20

        # -----------------------------------------------------
        # POWER PELLET FREEZE TIMER
        # -----------------------------------------------------

        self.frozen_timer = 0

    # ---------------------------------------------------------
    # ENEMY UPDATE / BFS
    # ---------------------------------------------------------

    def update(
        self,
        walls,
        player,
        rows,
        cols
    ):

        # Import BFS only when needed
        from game.maze import bfs

        # -----------------------------------------------------
        # FROZEN
        # -----------------------------------------------------

        if self.frozen_timer > 0:

            self.frozen_timer -= 1

            return

        # -----------------------------------------------------
        # NORMAL MOVEMENT
        # -----------------------------------------------------

        self.timer += 1

        if self.timer >= self.move_interval:

            self.timer = 0

            # Player's current maze cell
            player_row = player.rect.centery // CELL
            player_col = player.rect.centerx // CELL

            # BFS finds next step toward player
            step = bfs(
                walls,
                (self.r, self.c),
                (player_row, player_col),
                rows,
                cols
            )

            if step:

                dr, dc = step

                self.r += dr
                self.c += dc

                cx = self.c * CELL + CELL // 2
                cy = self.r * CELL + CELL // 2

                self.rect.center = (
                    cx,
                    cy
                )

    # ---------------------------------------------------------
    # FREEZE ENEMY
    # ---------------------------------------------------------

    def freeze(self, frames=300):

        # 60 FPS × 5 seconds = 300 frames
        self.frozen_timer = frames

    # ---------------------------------------------------------
    # DRAW ENEMY
    # ---------------------------------------------------------

    def draw(self, screen):

        # Blue when frozen
        if self.frozen_timer > 0:
            color = (70, 170, 255)
        else:
            color = self.color

        # Enemy body
        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=5
        )

        # Left eye
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                self.rect.x + 7,
                self.rect.y + 8
            ),
            4
        )

        # Right eye
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                self.rect.x + 17,
                self.rect.y + 8
            ),
            4
        )

        # Left pupil
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                self.rect.x + 8,
                self.rect.y + 8
            ),
            2
        )

        # Right pupil
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                self.rect.x + 18,
                self.rect.y + 8
            ),
            2
        )

        # Yellow ring when frozen
        if self.frozen_timer > 0:

            pygame.draw.circle(
                screen,
                (255, 255, 0),
                self.rect.center,
                17,
                2
            )