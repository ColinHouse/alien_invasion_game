class Settings():

    def __init__(self):
        # 初始化游戏设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)  # background

        self.ship_speed_factor = 0.5  # speed factor

        self.bullet_width = 6  # bullet width
        self.bullet_height = 14  # bullet length
        self.bullet_speed_factor = 0.4  # speed factor
        self.bullet_color = (60, 60, 60)  # bullet color
        self.max_bullets = 4  # bullet allowed showed on screen

        self.alien_speed_factor = 0.6  # alien speed factor
        self.fleet_drop_speed = 12  # alien fleet drop speed factor
        # fleet direction = 1 means right, 0 means go to the left
        self.fleet_direction = 1
        self.ship_limit = 2

        self.speedup_scale = 1.1  # speed up scale
        self.score_scale = 1.5  # score scale

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change as the game progresses
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.4
        self.alien_speed_factor = 0.6
        self.fleet_direction = 1

        self.alien_points = 50  # 计分

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
