# -*- coding: UTF-8 -*-
import pygame.font
from time import time


class Fps:
    '''帧率'''

    def __init__(self, ai_settings, screen, fps):
        '''初始化'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # 字体
        self.font = self.ai_settings.scorebaord_font
        # 渲染帧率
        self.prep_fps(fps)

    def prep_fps(self, fps):
        '''渲染帧率'''
        fps_str = f'{fps:,} fps'
        self.fps_image = self.font.render(fps_str, True,
                                          self.ai_settings.fps_text_color,
                                          self.ai_settings.bg_color)
        # 放置帧率于右下角
        self.fps_rect = self.fps_image.get_rect()
        self.fps_rect.left = 20
        self.fps_rect.bottom = self.screen_rect.bottom - 20

    def show_fps(self):
        '''显示帧率'''
        self.screen.blit(self.fps_image, self.fps_rect)

    def update_fps(self, stats, t1):
        self.prep_fps(stats.fps)
        stats.fps = 0
