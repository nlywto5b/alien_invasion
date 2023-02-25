# -*- coding: UTF-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import time, sleep
from pickle import load, dump


def check_keydown_events(event, ai_settings, screen, stats, sb, play_button,
                         ship, aliens, bullets, timer_info):
    '''响应按下按键'''
    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        stop_game(ai_settings, stats)
    elif event.key == pygame.K_p and (not stats.game_active):
        start_game(ai_settings, screen, stats, sb, timer_info, play_button,
                   ship, aliens, bullets)

def check_keyup_events(event, ship):
    '''响应松开按键'''
    if event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_d:
        ship.moving_right = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets, timer_info):
    '''响应按键和鼠标'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game(ai_settings, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, timer_info,
                              play_button, ship, aliens, bullets, mouse_x,
                              mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb,
                                 play_button, ship, aliens, bullets,
                                 timer_info)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb, timer_info, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    '''响应单击Play按钮事件'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and (not stats.game_active):
        start_game(ai_settings, screen, stats, sb, timer_info, play_button,
                   ship, aliens, bullets)


def start_game(ai_settings, screen, stats, sb, timer_info, play_button, ship,
               aliens, bullets):
    '''开始游戏'''
    # 重置动态设置
    ai_settings.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置统计信息
    stats.reset_stats()
    stats.game_active = True
    # 重置计分板
    sb.prep_images()
    # 重置时间
    timer_info.prep_timer()
    # 清空外星人和子弹
    aliens.empty()
    bullets.empty()
    # 创建新外星人
    ship.center_ship()
    create_fleet(ai_settings, screen, ship, aliens)

def stop_game(ai_settings, stats):
    '''结束游戏'''
    if stats.history_high_score < stats.high_score:
        write_hs(ai_settings, stats)
        back_up_score(ai_settings)
    sys.exit()


def write_hs(ai_settings, stats):
    '''写入最高分'''
    if ai_settings.difficulty == 1:
        ai_settings.info["easy_score"] = stats.high_score
    elif ai_settings.difficulty == 2:
        ai_settings.info["normal_score"] = stats.high_score
    elif ai_settings.difficulty == 3:
        ai_settings.info["difficult_score"] = stats.high_score
    with open('score.pickle', 'wb') as f:
        dump(ai_settings.info, f)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button, fps_info, timer_info):
    '''更新并重绘屏幕'''
    screen.fill(ai_settings.bg_color)
    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 显示计分板
    sb.show_score()
    # 显示时间
    timer_info.show_timer()
    # 显示帧率
    fps_info.show_fps()
    if not stats.game_active:
        play_button.draw_button(ai_settings)
    # 重绘屏幕
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''更新子弹'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens,
                                 bullets)


def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens,
                                 bullets):
    '''消灭被击杀的外星人'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    # 判断外星人是否被消灭
    if len(aliens) == 0:
        sleep(0.3)
        start_new_lvl(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_new_lvl(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''新等级初始化'''
    ship.center_ship()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ai_settings.increase_speed()
    # 提高等级
    stats.lvl += 1
    sb.prep_lvl()

def fire_bullet(ai_settings, screen, ship, bullets):
    '''发射子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_alien_x(ai_settings, alien_width):
    '''计算一行可容纳多少个外星人'''
    if ai_settings.difficulty == 1:
        available_space_x = ai_settings.screen_width - 2.5 * alien_width
    elif ai_settings.difficulty == 2:
        available_space_x = ai_settings.screen_width - 2 * alien_width
    elif ai_settings.difficulty == 3:
        available_space_x = ai_settings.screen_width - 1.5 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    if ai_settings.difficulty == 1:
        available_space_y = ai_settings.screen_height - 5 * alien_height - ship_height
    elif ai_settings.difficulty == 2:
        available_space_y = ai_settings.screen_height - 4 * alien_height - ship_height
    elif ai_settings.difficulty == 3:
        available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    return int(available_space_y / (2 * alien_height))


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建外星人'''
    alien = Alien(ai_settings, screen)
    alien.width = alien.rect.width
    alien.x = alien.width + 2 * alien.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''检查外星人是否碰到边缘并采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''改变外星人方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''响应飞船碰撞'''
    # 剩余飞船-1
    stats.ships_left -= 1
    if stats.ships_left > 0:
        sb.prep_ships()
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建新外星人
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''检查外星人是否撞到屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''检查外星人是否碰到边缘并更新位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测飞船与外星人的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    # 检测外星人与屏幕底端的碰撞
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    '''检查是否产生新新最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_fps_time(t1):
    '''检查和上一次更新fps时间是否相差1秒'''
    return int(round(time() - t1, 0)) == 1

def back_up_score(ai_settings):
    '''备份玩家数据'''
    with open('backup.pickle', 'wb') as f:
        dump(ai_settings.info, f)