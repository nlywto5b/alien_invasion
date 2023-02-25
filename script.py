# -*- coding: UTF-8 -*-
__version = 1, 4, 6
__author = 'Nly'

try:
    import pygame
    from pygame.sprite import Group
    from button import Button
    import game_function as gf
    from game_stats import GameStats
    from scoreboard import Scoreboard
    from settings import Settings
    from ship import Ship
    from time import time
    from fps import Fps
    from timer import Timer
except ImportError:  # 检测库/文件是否成功调用, 否则显示提示信息
    print('''请确认文件是否缺少! 
请确认pygame是否安装! ''')
else:

    # 游戏主体
    def run_game(difficulty_int, width, height):
        '''游戏主程序'''
        # 初始化pygame、设置和屏幕对象
        pygame.init()
        ai_settings = Settings(difficulty_int, int(width), int(height))
        screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('外星人大战')
        # 备份玩家分数
        gf.back_up_score(ai_settings)
        # 创建按钮
        play_button = Button(ai_settings, screen, '开始游戏 !')
        # 创建统计信息
        stats = GameStats(ai_settings)
        # 创建计分板
        sb = Scoreboard(ai_settings, screen, stats)
        # 创建帧率
        fps_info = Fps(ai_settings, screen, stats.fps)
        # 创建计时器
        timer_info = Timer(ai_settings, screen, stats)
        # 创建飞船
        ship = Ship(ai_settings, screen)
        # 创建子弹编组
        bullets = Group()
        # 创建外星人编组
        aliens = Group()
        # 创建外星人群
        gf.create_fleet(ai_settings, screen, ship, aliens)
        # 初始化时间
        t1 = time()
        # 开始游戏主循环
        while True:
            # 增加帧率
            stats.fps += 1
            if gf.check_fps_time(t1):
                t1 = time()
                # 更新帧率
                fps_info.update_fps(stats, t1)
            # 响应按键和鼠标
            gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                            aliens, bullets, timer_info)
            if stats.game_active:
                # 更新计时器
                timer_info.prep_timer()
            if stats.game_active:
                # 更新飞船、子弹、外星人位置
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                                 bullets)
            # 更新并重绘屏幕
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                             bullets, play_button, fps_info, timer_info)
            # 让最近绘制的屏幕可见
            pygame.display.flip()

    if __name__ == "__main__":
        '''程序开始'''
        import launcher  # 如果用户运行此文件时运行launcher.py
