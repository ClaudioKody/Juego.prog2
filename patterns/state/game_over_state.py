import pygame
from patterns.state.game_state import GameState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class GameOverState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font_title = pygame.font.Font(None, 54)
        self.font_subtitle = pygame.font.Font(None, 26)
        self.font_list = pygame.font.Font(None, 24)
        self.font_options = pygame.font.Font(None, 28)

    def enter(self):
        print("Entering Game Over State")

    def exit(self):
        print("Exiting Game Over State")

    def update(self):
        pass

    def draw(self, screen):
        # Fondo oscuro general
        screen.fill(BLACK)

        # Panel / Tarjeta central estética y adaptada para el desglose de niveles
        panel_width, panel_height = 460, 400
        panel_x = (SCREEN_WIDTH - panel_width) // 2
        panel_y = (SCREEN_HEIGHT - panel_height) // 2
        
        panel_surf = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
        panel_surf.fill((20, 20, 30, 230))  # Fondo semitransparente oscuro
        pygame.draw.rect(panel_surf, (255, 75, 75), (0, 0, panel_width, panel_height), 2, border_radius=12) # Borde rojo alerta
        screen.blit(panel_surf, (panel_x, panel_y))

        # Título
        title_text = self.font_title.render("¡FIN DEL JUEGO!", True, (255, 75, 75))
        screen.blit(title_text, (panel_x + (panel_width - title_text.get_width()) // 2, panel_y + 20))

        # Nivel actual donde se cayó en combate
        current_lvl = getattr(self.game, 'retry_level', 1)
        sub_text = self.font_subtitle.render(f"Te quedaste en el Nivel {current_lvl}", True, (200, 200, 200))
        screen.blit(sub_text, (panel_x + (panel_width - sub_text.get_width()) // 2, panel_y + 80))

        # --- Desglose de Niveles ---
        list_start_y = panel_y + 125
        list_header = self.font_list.render("--- ESTADO DE TU AVANCE ---", True, (0, 255, 230))
        screen.blit(list_header, (panel_x + (panel_width - list_header.get_width()) // 2, list_start_y))

        # Mostramos los niveles anteriores y el actual incompleto
        start_lvl = max(1, current_lvl - 2)
        end_lvl = current_lvl
        
        y_offset = list_start_y + 30
        for lvl in range(start_lvl, end_lvl + 1):
            if lvl < current_lvl:
                status_str = f"Nivel {lvl}: [ COMPLETADO ]"
                color = (0, 255, 0)  # Verde para completados
            else:
                status_str = f"Nivel {lvl}: [ INCOMPLETO / ACTUAL ]"
                color = (255, 255, 0)  # Amarillo para el actual

            lvl_row = self.font_list.render(status_str, True, color)
            screen.blit(lvl_row, (panel_x + 40, y_offset))
            y_offset += 25

        # Opciones inferiores
        restart_text = self.font_options.render("[ R ] Reiniciar Nivel Actual", True, WHITE)
        menu_text = self.font_options.render("[ M ] Menú Principal", True, WHITE)

        screen.blit(restart_text, (panel_x + (panel_width - restart_text.get_width()) // 2, panel_y + 285))
        screen.blit(menu_text, (panel_x + (panel_width - menu_text.get_width()) // 2, panel_y + 325))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.game.state_manager.change_state("playing")
            if event.key == pygame.K_m:
                self.game.state_manager.change_state("menu")
                