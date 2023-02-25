# -*- coding: UTF-8 -*-
import pygame.font


class Button:
    '''按钮'''

    def __init__(self, ai_settings, screen, msg):
        '''初始化'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.font = self.ai_settings.button_font
        # 创建按钮
        self.rect = pygame.Rect(0, 0, self.ai_settings.button_width,
                                self.ai_settings.button_height)
        self.rect.center = self.screen_rect.center
        # 渲染文本
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''渲染按钮文字'''
        self.msg_image = self.font.render(msg, True,
                                          self.ai_settings.button_text_color,
                                          self.ai_settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, ai_settings):
        self.screen.fill(self.ai_settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
