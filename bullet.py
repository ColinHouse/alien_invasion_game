import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # 对子弹进行管理的类

    def __init__(self, ai_settings, screen, ship):
        super().__init__()  # 继承Sprite类: Sprite可以同时操作编组中的所有相关元素
        self.screen = screen

        # 在(0,0)处创建正确的矩形，再将其设置在合适的位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹位置
        self.y = float(ship.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 向上移动子弹并更新子弹y轴坐标的小数值
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
