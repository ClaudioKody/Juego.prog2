import pygame
from patterns.state.game_state import GameState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from patterns.observer.game_stats import GameStats

class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font_title = pygame.font.Font(None, 64)
        self.font_option = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 24)

        # Opciones reales según los estados que tenés creados
        self.options = ["JUGAR", "SALIR"]
        self.selected_index = 0
        self.stats = GameStats()

    def enter(self):
        print("Entering Menu State")
        self.stats.high_score = self.stats.load_high_score()

    def exit(self):
        print("Exiting Menu State")

    def update(self):
        pass

    def draw(self, screen):
        # Fondo oscuro/elegante (sin estrellas/nieve)
        screen.fill((15, 15, 25))

        # 1. Título Limpio con Sombra Sutil
        shadow_title = self.font_title.render("RETRO SHOOTER", True, (0, 80, 120))
        title_text = self.font_title.render("RETRO SHOOTER", True, (0, 255, 230))
        
        title_x = SCREEN_WIDTH // 2 - title_text.get_width() // 2
        screen.blit(shadow_title, (title_x + 3, 83))
        screen.blit(title_text, (title_x, 80))

        # Línea divisora
        pygame.draw.line(screen, (0, 255, 230), (SCREEN_WIDTH // 2 - 120, 150), (SCREEN_WIDTH // 2 + 120, 150), 2)

        # 2. Selector de Opciones Centrado y Proporcional
        start_y = 240
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                color = (255, 215, 0) # Dorado al seleccionar
                text_str = f"▶  {option}  ◀"
            else:
                color = WHITE
                text_str = option
            
            opt_text = self.font_option.render(text_str, True, color)
            screen.blit(opt_text, (SCREEN_WIDTH // 2 - opt_text.get_width() // 2, start_y + i * 60))

        # 3. High Score discreto en el pie de página
        hs_text = self.font_small.render(f"BEST SCORE: {self.stats.high_score}", True, (150, 150, 150))
        screen.blit(hs_text, (SCREEN_WIDTH // 2 - hs_text.get_width() // 2, SCREEN_HEIGHT - 40))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                if self.selected_index == 0:
                    self.game.state_manager.change_state("playing")
                elif self.selected_index == 1:
                    pygame.quit()
                    exit()
                    