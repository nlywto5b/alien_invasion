# -*- coding: UTF-8 -*-
import pygame.font
from time import time, gmtime, strftime
from math import floor


class Timer:
    '''计时器'''

    def __init__(self, ai_settings, screen, stats):
        '''初始化'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # 字体
        self.font = self.ai_settings.timer_font
        # 渲染计时器
        self.prep_timer()

    def prep_timer(self):
        '''渲染计时器'''
        now_time = time() - self.stats.start_time
        now_float_time = int(round(now_time - floor(now_time), 2) * 100)
        now_time = gmtime(now_time)
        # 补0
        m = ('0' if now_time.tm_min // 10 == 0 else '') + str(now_time.tm_min)
        s = ('0' if now_time.tm_sec // 10 == 0 else '') + str(now_time.tm_sec)
        f = ('0' if now_float_time // 10 == 0 else '') + str(now_float_time)
        timer_str = '{}:{}.{}'.format(m, s, f)
        self.timer_image = self.font.render(timer_str, True,
                                            self.ai_settings.timer_text_color,
                                            self.ai_settings.bg_color)
        # 放置计时器于顶部中央
        self.timer_rect = self.timer_image.get_rect()
        self.timer_rect.centerx = self.screen_rect.centerx
        self.timer_rect.top = 20

    def show_timer(self):
        '''显示计分板'''
        self.screen.blit(self.timer_image, self.timer_rect)
