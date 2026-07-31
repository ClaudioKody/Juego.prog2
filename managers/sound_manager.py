import pygame
import math
import array
import random
from patterns.singleton.sound_manager import SoundManager

class SoundManagerFacade:
    def __init__(self):
        self._sound_manager = SoundManager()
        self.sounds = {}
        self._init_procedural_sounds()

    def _init_procedural_sounds(self):
        """Genera sonidos sintetizados de 8-bits por código."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
            
            # Sonido de Láser
            duration_l = 0.1
            samples_l = int(22050 * duration_l)
            buf_l = array.array('h')
            for i in range(samples_l):
                freq = 800 - (i / samples_l) * 400
                buf_l.append(int(16000 * math.sin(2 * math.pi * freq * (i / 22050))))
            self.sounds['laser'] = pygame.mixer.Sound(buffer=buf_l)

            # Sonido de Explosión
            duration_e = 0.2
            samples_e = int(22050 * duration_e)
            buf_e = array.array('h')
            for i in range(samples_e):
                decay = 1.0 - (i / samples_e)
                buf_e.append(int(random.randint(-16000, 16000) * decay))
            self.sounds['explosion'] = pygame.mixer.Sound(buffer=buf_e)

        except Exception as e:
            print(f"Advertencia: No se pudo iniciar el audio: {e}")

    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].play(loops=loops)
        else:
            # Fallback al singleton tradicional si se cargó un archivo externo
            self._sound_manager.play_sound(name, loops)

    def load_sound(self, name, path):
        self._sound_manager.load_sound(name, path)

    def stop_sound(self, name):
        self._sound_manager.stop_sound(name)

    def set_volume(self, name, volume):
        self._sound_manager.set_volume(name, volume)
        