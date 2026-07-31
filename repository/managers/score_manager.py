
from repository.database.score_repository import ScoreRepository

class ScoreManager:
    def __init__(self):
        self.score_repository = ScoreRepository()

    def add_score(self, player_name, score):
        self.score_repository.save_score(player_name, score)

    def get_top_scores(self, limit=10):
        return self.score_repository.get_high_scores(limit)
