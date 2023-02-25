# -*- coding: UTF-8 -*-
import pygame
import tkinter as tk
from tkinter import messagebox
from game_function import get_score


class Settings:
    '''设置'''

    def __init__(self, difficulty, width, height):
        '''初始化游戏静态设置'''
        # 屏幕设置
        self.screen_width = width
        self.screen_height = height
        self.bg_color = 230, 230, 230
        # 难度设置&信息
        self.score = get_score()
        self.difficulty = difficulty  # 1:简单, 2:普通, 3:困难
        # 飞船设置
        if self.difficulty == 1:
            self.ship_limit = 4
        elif self.difficulty == 2:
            self.ship_limit = 3
        elif self.difficulty == 3:
            self.ship_limit = 2
        self.ship_speed_factor = 5
        # 子弹设置
        if self.difficulty == 1:
            self.bullet_width_limit = 250
        elif self.difficulty == 2:
            self.bullet_width_limit = 200
        elif self.difficulty == 3:
            self.bullet_width_limit = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 7
        self.bullet_speed_factor = 10
        # 外星人设置
        if self.difficulty == 1:
            self.fleet_drop_speed = 20
        elif self.difficulty == 2:
            self.fleet_drop_speed = 25
        elif self.difficulty == 3:
            self.fleet_drop_speed = 26
        # 按钮设置
        self.button_width = self.screen_width // 4
        self.button_height = 50
        self.button_color = 0, 255, 0
        self.button_text_color = 255, 255, 255
        self.button_font = pygame.font.SysFont('Kaiti', 45)
        # 加速设置
        if self.difficulty == 1:
            self.speedup_scale = 1.05
        elif self.difficulty == 2:
            self.speedup_scale = 1.1
        elif self.difficulty == 3:
            self.speedup_scale = 1.15
        self.score_scale = 1.3
        # 计分板设置
        self.scorebaord_text_color = 30, 30, 30
        self.scorebaord_font = pygame.font.SysFont('Kaiti', 30)
        # 帧率设置
        self.fps_text_color = 30, 30, 30
        self.fps_font = pygame.font.SysFont('Kaiti', 30)
        # 计时器设置
        self.timer_text_color = 30, 30, 30
        self.timer_font = pygame.font.SysFont('Kaiti', 30)
        # 暂停设置
        self.allow_suspend = True
        # 初始化动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化动态设置'''
        # 子弹设置
        self.bullet_width = 3
        # 外星人设置
        if self.difficulty == 1:
            self.alien_speed_factor = 1.4
        elif self.difficulty == 2:
            self.alien_speed_factor = 1.5
        elif self.difficulty == 3:
            self.alien_speed_factor = 1.65
        self.fleet_direction = 1  # 1 - left    2 - right
        # 计分板设置
        self.alien_points = 50

    def increase_speed(self):
        '''加速设置'''
        self.alien_speed_factor *= self.speedup_scale  # 增加外星人速度
        self.alien_points = int(self.alien_points *
                                self.score_scale)  # 增加外星人分数
        if self.bullet_width <= self.bullet_width_limit:  # 在没到宽度上限时增加子弹数量
            self.bullet_width *= self.speedup_scale
