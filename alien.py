# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''外星人'''

    def __init__(self, ai_settings, screen):
        '''初始化'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 将外星人放置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        '''绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''检测外星人是否碰到边缘'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def update(self):
        '''移动外星人'''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
