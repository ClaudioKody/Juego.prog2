
import pygame
from patterns.state.game_state import GameState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class PausedState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)

    def enter(self):
        print("Entering Paused State")

    def exit(self):
        print("Exiting Paused State")

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)
        title_text = self.font.render("PAUSA", True, WHITE)
        resume_text = self.small_font.render("Presiona R para Reanudar", True, WHITE)
        menu_text = self.small_font.render("Presiona M para Menú Principal", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.game.state_manager.change_state("playing")
            if event.key == pygame.K_m:
                self.game.state_manager.change_state("menu")
