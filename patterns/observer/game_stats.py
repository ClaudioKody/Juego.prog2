import os
from patterns.observer.observer import Subject

class GameStats(Subject):
    def __init__(self):
        super().__init__()
        self._score = 0
        self._lives = 3
        self._level = 1
        # Sin límite de nivel para que sea infinito
        self._enemies_killed = 0
        self._enemies_target = 10  # Nivel 1 arranca pidiendo 10 bajas
        self.high_score_file = "highscore.txt"
        self.high_score = self.load_high_score()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        if self._score > self.high_score:
            self.high_score = self._score
            self.save_high_score()
        self.notify(score=self._score, lives=self._lives, level=self._level)

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        self._lives = value
        self.notify(score=self._score, lives=self._lives, level=self._level)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self._enemies_target = 10 + (self._level - 1) * 5
        self._enemies_killed = 0
        self.notify(score=self._score, lives=self._lives, level=self._level)

    @property
    def enemies_killed(self):
        return self._enemies_killed

    @property
    def enemies_target(self):
        return self._enemies_target

    def add_kill(self):
        """Suma puntos por baja y evalúa si se completó el nivel."""
        self._enemies_killed += 1
        self.score += 100
        if self._enemies_killed >= self._enemies_target:
            return True
        return False

    def next_level(self):
        """Pasa de nivel infinitamente incrementando la dificultad y la meta."""
        self._level += 1
        self._enemies_killed = 0
        self._enemies_target = 10 + (self._level - 1) * 5  # Niveles cada vez más largos
        self.notify(score=self._score, lives=self._lives, level=self._level)

    def is_game_won(self):
        # Al ser infinito, ya no hay una victoria por fin de niveles
        return False

    def reset(self):
        self._score = 0
        self._lives = 3
        self._level = 1
        self._enemies_killed = 0
        self._enemies_target = 10
        self.notify(score=self._score, lives=self._lives, level=self._level)

    def load_high_score(self):
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, "r") as f:
                    return int(f.read().strip())
            except ValueError:
                return 0
        return 0

    def save_high_score(self):
        try:
            with open(self.high_score_file, "w") as f:
                f.write(str(self.high_score))
        except Exception as e:
            print(f"Error guardando high score: {e}")
            