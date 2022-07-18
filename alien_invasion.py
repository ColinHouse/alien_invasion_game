import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group  # 创建一个编组Group存储发射出去的所有子弹、外星人
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置

    ai_settings = Settings()  # 设置实例化

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 创建一个名为screen的窗口尺寸
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)  # 船实例化
    bullets = Group()  # 子弹编组实例化
    # alien = Alien(ai_settings, screen) # 外星人实例化
    aliens = Group()  # 外星人编组实例化
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")  # play button

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)  # check_events
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)  # update_bullets
            gf.update_aliens(ai_settings, screen, stats, sb,
                             ship, aliens, bullets)  # update_aliens
        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)  # update_screen


run_game()
