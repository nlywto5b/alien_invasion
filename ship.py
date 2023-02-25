# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''飞船'''

    def __init__(self, ai_settings, screen):
        '''初始化'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞船放置在屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        '''根据移动标志改变飞船位置'''
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor

    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''居中飞船'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
