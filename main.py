
import pygame
from core.game import Game
from patterns.state.menu_state import MenuState
from patterns.state.playing_state import PlayingState
from patterns.state.paused_state import PausedState
from patterns.state.game_over_state import GameOverState

def main():
    game = Game()

    # Registrar estados del juego
    game.state_manager.add_state("menu", MenuState(game))
    game.state_manager.add_state("playing", PlayingState(game))
    game.state_manager.add_state("paused", PausedState(game))
    game.state_manager.add_state("game_over", GameOverState(game))

    # Establecer el estado inicial
    game.state_manager.change_state("menu")

    game.run()

if __name__ == "__main__":
    main()
