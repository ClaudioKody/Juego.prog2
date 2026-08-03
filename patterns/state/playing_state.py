import random
import pygame
from patterns.state.game_state import GameState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from entities.player import Player
from entities.bullet import Bullet
from patterns.factory.enemy_factory import EnemyFactory
from patterns.factory.bullet_factory import BulletFactory
from patterns.observer.game_stats import GameStats
from utils.constants import ENEMY_SPAWN_EVENT
from managers.sound_manager import SoundManagerFacade

class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.enemy_factory = EnemyFactory()
        self.bullet_factory = BulletFactory()
        self.game_stats = GameStats()
        self.sound_manager = SoundManagerFacade()

        self.showing_level_cleared = False
        self.level_cleared_timer = 0
        
        # Guardamos el nivel actual para poder reiniciar en él si se pierde
        self.saved_level = 1

    def enter(self):
        print("Entering Playing State")
        # Si venimos de Game Over con nivel guardado, lo restauramos
        if hasattr(self.game, 'retry_level') and self.game.retry_level:
            self.game_stats.level = self.game.retry_level
            self.game.retry_level = None
        else:
            self.game_stats.reset()
            
        self.player.lives = 3  # Aseguramos 3 vidas al entrar/reiniciar
        self.game_stats.lives = 3
        self.apply_level_difficulty()

    def exit(self):
        print("Exiting Playing State")
        pygame.time.set_timer(ENEMY_SPAWN_EVENT, 0)

    def apply_level_difficulty(self):
        """Ajusta la frecuencia de los enemigos de forma progresiva según el nivel."""
        # Cuanto mayor sea el nivel, menor el tiempo de espera (más enemigos caen)
        spawn_time = max(300, 1500 - (self.game_stats.level - 1) * 200)
        pygame.time.set_timer(ENEMY_SPAWN_EVENT, spawn_time)

    def update(self):
        # Transición al ganar un nivel
        if self.showing_level_cleared:
            if pygame.time.get_ticks() - self.level_cleared_timer > 2000:
                self.showing_level_cleared = False
                self.enemies.empty()
                self.enemy_bullets.empty()
                self.player_bullets.empty()
                self.apply_level_difficulty()
            return

        self.all_sprites.update()

        # Disparos enemigos (más agresivos según el nivel)
        for enemy in self.enemies:
            shoot_chance = 0.006 + (self.game_stats.level * 0.003)
            if random.random() < shoot_chance:
                bullet = self.bullet_factory.create_product(enemy.rect.centerx, enemy.rect.bottom, -1)
                self.enemy_bullets.add(bullet)
                self.all_sprites.add(bullet)

        # Colisiones: Balas del jugador destruyen enemigos al instante (1 solo tiro)
        hits = pygame.sprite.groupcollide(self.enemies, self.player_bullets, True, True)
        for hit in hits:
            self.sound_manager.play_sound('explosion')
            level_completed = self.game_stats.add_kill()

            if level_completed:
                self.game_stats.next_level()
                self.showing_level_cleared = True
                self.level_cleared_timer = pygame.time.get_ticks()

        # Colisiones: Balas enemigas impactan al jugador
        hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        for hit in hits:
            self.sound_manager.play_sound('explosion')
            if self.player.take_damage():
                # Guardamos el nivel actual antes de ir al Game Over
                self.game.retry_level = self.game_stats.level
                self.game.state_manager.change_state("game_over")
            self.game_stats.lives = self.player.lives

        # Colisiones: Enemigos chocan contra el jugador
        hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for hit in hits:
            self.sound_manager.play_sound('explosion')
            if self.player.take_damage():
                # Guardamos el nivel actual antes de ir al Game Over
                self.game.retry_level = self.game_stats.level
                self.game.state_manager.change_state("game_over")
            self.game_stats.lives = self.player.lives

    def draw(self, screen):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)

        # HUD superior
        font = pygame.font.Font(None, 32)
        score_text = font.render(f"Score: {self.game_stats.score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        kills_text = font.render(
            f"Nivel {self.game_stats.level} | Meta: {self.game_stats.enemies_killed}/{self.game_stats.enemies_target}", 
            True, (0, 255, 230)
        )

        screen.blit(score_text, (10, 10))
        screen.blit(kills_text, (SCREEN_WIDTH // 2 - kills_text.get_width() // 2, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))

        # Cartel de Nivel Completado
        if self.showing_level_cleared:
            font_big = pygame.font.Font(None, 52)
            msg = font_big.render(f"¡NIVEL {self.game_stats.level - 1} COMPLETADO!", True, (255, 255, 0))
            rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(msg, rect)

    def handle_event(self, event):
        if self.showing_level_cleared:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b_center = self.bullet_factory.create_product(self.player.rect.centerx, self.player.rect.top, 1)
                b_left = Bullet(self.player.rect.centerx, self.player.rect.top, 1, speed_x=-3)
                b_right = Bullet(self.player.rect.centerx, self.player.rect.top, 1, speed_x=3)

                self.player_bullets.add(b_center, b_left, b_right)
                self.all_sprites.add(b_center, b_left, b_right)
                self.sound_manager.play_sound('laser')

            if event.key == pygame.K_ESCAPE:
                self.game.state_manager.change_state("paused")
                
        if event.type == ENEMY_SPAWN_EVENT:
            enemy = self.enemy_factory.create_product(random.randint(0, SCREEN_WIDTH - 40), -40)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
            