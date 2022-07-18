import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()  # 获取图片矩形的信息
        self.screen_rect = screen.get_rect()  # 获取屏幕矩形的信息

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = [float(self.rect.centerx), float(self.rect.centery)]

        # 设定移动标志
        self.moving_right = False
        self.moving_down = False
        self.moving_up = False
        self.moving_left = False

    def update(self):
        # 根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center[1] += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center[1] -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def blitme(self):
        # 在指定位置打印飞船
        self.screen.blit(self.image, self.rect)
        # 根据self.rect的指定位置将图像绘制到屏幕上

    def center_ship(self):
        # 让飞船在屏幕上居中
        self.center[0] = self.screen_rect.centerx
        self.center[1] = self.screen_rect.bottom - 0.5 * self.image.get_height()