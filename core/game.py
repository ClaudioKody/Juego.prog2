
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, SCREEN, CLOCK
from core.state_manager import StateManager
from core.event_manager import EventManager
from patterns.singleton.sound_manager import SoundManager

class Game:
    def __init__(self):
        self.running = True
        self.state_manager = StateManager()
        self.event_manager = EventManager()
        self.sound_manager = SoundManager()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.event_manager.handle_event(event, self.state_manager.get_current_state())

            current_state = self.state_manager.get_current_state()
            current_state.update()
            current_state.draw(SCREEN)

            pygame.display.flip()
            CLOCK.tick(FPS)

        pygame.quit()
