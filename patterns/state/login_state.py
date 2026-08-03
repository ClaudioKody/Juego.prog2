import pygame
from patterns.state.game_state import GameState

class LoginState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.modo = "MENU"
        self.username = ""
        self.mensaje_error = ""
        self.font_title = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        self.color_bg = (30, 30, 40)
        self.color_box = (60, 60, 80)
        self.color_active = (100, 200, 100)
        self.color_text = (255, 255, 255)
        self.color_btn = (70, 130, 180)

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.modo != "MENU":
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                elif event.key == pygame.K_RETURN:
                    self.procesar_ingreso()
                else:
                    if len(self.username) < 15 and event.unicode.isalnum():
                        self.username += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.modo == "MENU":
                if 300 <= pos[0] <= 500 and 250 <= pos[1] <= 310:
                    self.modo = "REGISTRAR"
                    self.mensaje_error = ""
                    self.username = ""
                elif 300 <= pos[0] <= 500 and 330 <= pos[1] <= 390:
                    self.modo = "INICIAR"
                    self.mensaje_error = ""
                    self.username = ""
            else:
                if 50 <= pos[0] <= 150 and 500 <= pos[1] <= 540:
                    self.modo = "MENU"
                    self.username = ""
                    self.mensaje_error = ""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            else:
                self.handle_event(event)

    def procesar_ingreso(self):
        if not self.username.strip():
            self.mensaje_error = "El nombre no puede estar vacio."
            return
        try:
            from repository.database.user_repository import UserRepository
            user_repo = UserRepository()
            
            if self.modo == "REGISTRAR":
                print("PASO 1")
                level, max_score = user_repo.obtener_o_crear_usuario(self.username)
                print("PASO 2")
                self.game.current_user = self.username
                self.game.current_level = level
                self.game.max_score = max_score
                print("PASO 3")
                self.game.state_manager.change_state("menu")
                print("PASO 4")
                
            elif self.modo == "INICIAR":
                print("PASO INICIAR 1")
                # Corregido para usar el repositorio de forma limpia y evitar errores de sintaxis SQL
                level, max_score = user_repo.obtener_o_crear_usuario(self.username)
                print("PASO INICIAR 2")
                self.game.current_user = self.username
                self.game.current_level = level
                self.game.max_score = max_score
                print("PASO INICIAR 3")
                self.game.state_manager.change_state("menu")
                print("PASO INICIAR 4")
                
        except Exception as e:
            print(f"ERROR CRITICO EN LOGIN: {e}")
            self.mensaje_error = f"Error: {str(e)[:30]}"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(self.color_bg)
        if self.modo == "MENU":
            title = self.font_title.render("¡BIENVENIDO AL JUEGO!", True, (255, 215, 0))
            screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 120))
            
            pygame.draw.rect(screen, self.color_btn, (300, 250, 200, 60), border_radius=10)
            text_reg = self.font_text.render("Registrarse", True, self.color_text)
            screen.blit(text_reg, (400 - text_reg.get_width() // 2, 268))
            
            pygame.draw.rect(screen, self.color_btn, (300, 330, 200, 60), border_radius=10)
            text_ini = self.font_text.render("Iniciar Sesión", True, self.color_text)
            screen.blit(text_ini, (400 - text_ini.get_width() // 2, 348))
        else:
            titulo_modo = "REGISTRO DE NUEVO USUARIO" if self.modo == "REGISTRAR" else "INICIAR SESIÓN"
            title = self.font_title.render(titulo_modo, True, (255, 255, 255))
            screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))
            
            instruction = self.font_small.render("Escribí tu nombre de usuario y presioná ENTER:", True, (200, 200, 200))
            screen.blit(instruction, (screen.get_width() // 2 - instruction.get_width() // 2, 180))
            
            box_rect = pygame.Rect(250, 240, 300, 50)
            pygame.draw.rect(screen, self.color_box, box_rect, border_radius=8)
            pygame.draw.rect(screen, self.color_active, box_rect, 2, border_radius=8)
            
            txt_surface = self.font_text.render(self.username, True, self.color_text)
            screen.blit(txt_surface, (box_rect.x + 15, box_rect.y + 12))
            
            if self.mensaje_error:
                err_surface = self.font_small.render(self.mensaje_error, True, (255, 100, 100))
                screen.blit(err_surface, (screen.get_width() // 2 - err_surface.get_width() // 2, 310))
                
            pygame.draw.rect(screen, (100, 60, 60), (50, 500, 100, 40), border_radius=5)
            txt_volver = self.font_small.render("Volver", True, self.color_text)
            screen.blit(txt_volver, (100 - txt_volver.get_width() // 2, 510))