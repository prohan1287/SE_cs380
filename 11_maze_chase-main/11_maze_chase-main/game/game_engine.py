import pygame
from game.maze import generate_maze, CELL
from game.entities import Player, Enemy


COLS, ROWS = 13, 11
WIDTH = COLS * CELL
HEIGHT = ROWS * CELL + 50
FPS = 60


class GameEngine:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Chase")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("monospace", 22)
        self.big_font = pygame.font.SysFont(
            "monospace",
            38,
            bold=True
        )

        self.reset()

    def reset(self):

        # Generate maze
        self.walls = generate_maze(COLS, ROWS)

        # Player
        self.player = Player(0, 0)

        # =====================================================
        # TASK 1: THREE ENEMIES
        # =====================================================

        self.enemies = [
            Enemy(ROWS - 1, COLS - 1, (220, 60, 60)),
            Enemy(ROWS - 1, 0, (180, 60, 220)),
            Enemy(0, COLS - 1, (220, 140, 40))
        ]

        # =====================================================
        # EXIT
        # =====================================================

        self.exit_rect = pygame.Rect(
            (COLS // 2) * CELL + 5,
            (ROWS // 2) * CELL + 5,
            CELL - 10,
            CELL - 10
        )

        # =====================================================
        # TASK 3: POWER PELLET
        # =====================================================

        self.pellet_cell = (
            ROWS - 2,
            COLS // 2
        )

        self.pellet_rect = pygame.Rect(
            self.pellet_cell[1] * CELL + CELL // 2 - 8,
            self.pellet_cell[0] * CELL + CELL // 2 - 8,
            16,
            16
        )

        self.pellet_active = True

        # =====================================================
        # TASK 4: SURVIVAL SCORE
        # =====================================================

        self.score = 0

        # Time when game started
        self.start_time = pygame.time.get_ticks()

        # Difficulty level
        self.speed_tier = 0

        # Game state
        self.caught = False
        self.won = False

    # =========================================================
    # EVENTS
    # =========================================================

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    self.reset()

        return True

    # =========================================================
    # UPDATE
    # =========================================================

    def update(self):

        if self.caught or self.won:
            return

        # -----------------------------------------------------
        # PLAYER MOVEMENT
        # -----------------------------------------------------

        keys = pygame.key.get_pressed()

        self.player.move(
            keys,
            self.walls,
            ROWS,
            COLS
        )

        # -----------------------------------------------------
        # TASK 4: SURVIVAL SCORE
        # -----------------------------------------------------

        self.score += 1

        # -----------------------------------------------------
        # TASK 2: INCREASE ENEMY SPEED EVERY 15 SECONDS
        # -----------------------------------------------------

        elapsed_ms = pygame.time.get_ticks() - self.start_time

        elapsed_seconds = elapsed_ms // 1000

        new_tier = elapsed_seconds // 15

        if new_tier != self.speed_tier:

            self.speed_tier = new_tier

            # Smaller interval = faster enemies
            new_interval = max(
                5,
                20 - (self.speed_tier * 2)
            )

            for enemy in self.enemies:
                enemy.move_interval = new_interval

        # -----------------------------------------------------
        # TASK 1: UPDATE ALL THREE ENEMIES
        # -----------------------------------------------------

        for enemy in self.enemies:

            enemy.update(
                self.walls,
                self.player,
                ROWS,
                COLS
            )

        # -----------------------------------------------------
        # TASK 3: POWER PELLET
        # -----------------------------------------------------

        if (
            self.pellet_active
            and self.player.rect.colliderect(
                self.pellet_rect
            )
        ):

            self.pellet_active = False

            # Freeze every enemy for 5 seconds
            for enemy in self.enemies:
                enemy.freeze(300)

        # -----------------------------------------------------
        # ENEMY COLLISION
        # -----------------------------------------------------

        for enemy in self.enemies:

            if self.player.rect.colliderect(enemy.rect):

                # Frozen enemies cannot catch the player
                if enemy.frozen_timer <= 0:
                    self.caught = True
                    break

        # -----------------------------------------------------
        # EXIT COLLISION
        # -----------------------------------------------------

        if self.player.rect.colliderect(self.exit_rect):
            self.won = True

    # =========================================================
    # DRAW
    # =========================================================

    def draw(self):

        self.screen.fill((230, 220, 210))

        # -----------------------------------------------------
        # DRAW MAZE
        # -----------------------------------------------------

        wc = (50, 40, 60)

        for r in range(ROWS):

            for c in range(COLS):

                x = c * CELL
                y = r * CELL

                w = self.walls[r][c]

                # Top wall
                if w[0]:
                    pygame.draw.line(
                        self.screen,
                        wc,
                        (x, y),
                        (x + CELL, y),
                        3
                    )

                # Bottom wall
                if w[1]:
                    pygame.draw.line(
                        self.screen,
                        wc,
                        (x, y + CELL),
                        (x + CELL, y + CELL),
                        3
                    )

                # Right wall
                if w[2]:
                    pygame.draw.line(
                        self.screen,
                        wc,
                        (x + CELL, y),
                        (x + CELL, y + CELL),
                        3
                    )

                # Left wall
                if w[3]:
                    pygame.draw.line(
                        self.screen,
                        wc,
                        (x, y),
                        (x, y + CELL),
                        3
                    )

        # -----------------------------------------------------
        # EXIT
        # -----------------------------------------------------

        pygame.draw.rect(
            self.screen,
            (80, 200, 80),
            self.exit_rect,
            border_radius=4
        )

        lbl = self.font.render(
            "EXIT",
            True,
            (20, 80, 20)
        )

        self.screen.blit(
            lbl,
            (
                self.exit_rect.x + 2,
                self.exit_rect.y + 6
            )
        )

        # -----------------------------------------------------
        # TASK 3: POWER PELLET
        # -----------------------------------------------------

        if self.pellet_active:

            pygame.draw.circle(
                self.screen,
                (255, 220, 40),
                self.pellet_rect.center,
                8
            )

            pygame.draw.circle(
                self.screen,
                (255, 245, 150),
                self.pellet_rect.center,
                12,
                2
            )

        # -----------------------------------------------------
        # PLAYER
        # -----------------------------------------------------

        self.player.draw(self.screen)

        # -----------------------------------------------------
        # ALL ENEMIES
        # -----------------------------------------------------

        for enemy in self.enemies:
            enemy.draw(self.screen)

        # -----------------------------------------------------
        # HUD
        # -----------------------------------------------------

        hud = pygame.Rect(
            0,
            ROWS * CELL,
            WIDTH,
            50
        )

        pygame.draw.rect(
            self.screen,
            (30, 30, 50),
            hud
        )

        survived_seconds = self.score // 60

        info = self.font.render(
            f"Survived: {survived_seconds}s   "
            f"Speed: {self.speed_tier}   "
            f"R=Restart",
            True,
            (200, 200, 200)
        )

        self.screen.blit(
            info,
            (
                8,
                ROWS * CELL + 14
            )
        )

        # -----------------------------------------------------
        # GAME OVER
        # -----------------------------------------------------

        if self.caught:
            self._overlay(
                "CAUGHT!",
                (220, 60, 60)
            )

        # -----------------------------------------------------
        # WIN
        # -----------------------------------------------------

        if self.won:
            self._overlay(
                "ESCAPED!",
                (80, 220, 80)
            )

        pygame.display.flip()

    # =========================================================
    # OVERLAY
    # =========================================================

    def _overlay(self, text, color):

        surf = pygame.Surface(
            (WIDTH, ROWS * CELL),
            pygame.SRCALPHA
        )

        surf.fill(
            (0, 0, 0, 140)
        )

        self.screen.blit(
            surf,
            (0, 0)
        )

        msg = self.big_font.render(
            text,
            True,
            color
        )

        final_score = self.font.render(
            f"Survived: {self.score // 60}s",
            True,
            (255, 255, 255)
        )

        sub = self.font.render(
            "Press R to Restart",
            True,
            (200, 200, 200)
        )

        self.screen.blit(
            msg,
            (
                WIDTH // 2 - msg.get_width() // 2,
                ROWS * CELL // 2 - 55
            )
        )

        self.screen.blit(
            final_score,
            (
                WIDTH // 2 - final_score.get_width() // 2,
                ROWS * CELL // 2
            )
        )

        self.screen.blit(
            sub,
            (
                WIDTH // 2 - sub.get_width() // 2,
                ROWS * CELL // 2 + 35
            )
        )

    # =========================================================
    # MAIN LOOP
    # =========================================================

    def run(self):

        running = True

        while running:

            running = self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)

        pygame.quit()