
import pygame

class SoundManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SoundManager, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if not self.initialized:
            pygame.mixer.init()
            self.sounds = {}
            self.initialized = True

    def load_sound(self, name, path):
        if name not in self.sounds:
            self.sounds[name] = pygame.mixer.Sound(path)

    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].play(loops)

    def stop_sound(self, name):
        if name in self.sounds:
            self.sounds[name].stop()

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def get_instance(self):
        return self._instance
