# -*- coding: UTF-8 -*-
from time import time


class GameStats:
    '''跟踪游戏统计信息'''

    def __init__(self, ai_settings):
        '''初始化'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏状态
        self.game_active = False
        # 最高分
        if ai_settings.difficulty == 1:
            self.history_high_score = ai_settings.info['easy_score']
        elif ai_settings.difficulty == 2:
            self.history_high_score = ai_settings.info['normal_score']
        elif ai_settings.difficulty == 3:
            self.history_high_score = ai_settings.info['difficult_score']
        self.high_score = self.history_high_score
        # 帧率
        self.fps = 0

    def reset_stats(self):
        '''初始化动态统计信息'''
        # 剩余飞船数
        self.ships_left = self.ai_settings.ship_limit
        # 分数
        self.score = 0
        # 等级
        self.lvl = 1
        # 游戏开始时间 (for timer)
        self.start_time = time()
