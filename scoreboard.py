# -*- coding: UTF-8 -*-
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    '''计分板'''

    def __init__(self, ai_settings, screen, stats):
        '''初始化'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # 字体
        self.font = self.ai_settings.scorebaord_font
        # 渲染计分板
        self.prep_images()

    def prep_score(self):
        '''渲染计分板'''
        rounded_score = round(self.stats.score, -1)
        score_str = '{}: {:,}'.format('分数', rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.ai_settings.scorebaord_text_color,
            self.ai_settings.bg_color)
        # 放置计分板于左上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''渲染最高分'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{}: {:,}'.format('最高分', high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.ai_settings.scorebaord_text_color,
            self.ai_settings.bg_color)
        # 放置最高分于右上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    def prep_lvl(self):
        '''渲染等级'''
        self.lvl_image = self.font.render(
            '{}: {:,}'.format('等级', self.stats.lvl), True,
            self.ai_settings.scorebaord_text_color, self.ai_settings.bg_color)
        # 放置等级于得分下
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.left = 20
        self.lvl_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''渲染剩余飞船'''
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.right = self.screen_rect.right - (
                10 + ship_num * ship.rect.width)
            ship.rect.top = self.high_score_rect.bottom + 10
            self.ships.add(ship)

    def prep_images(self):
        '''渲染计分板'''
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ships()

    def show_score(self):
        '''显示计分板'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)
