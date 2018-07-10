#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,re,math
import pygame as pg
from bullet import Bullet
from alien import Alien

def check_keydown_events (event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key==pg.K_RIGHT:
        ship.moving_right=True
    elif event.key==pg.K_LEFT:
        ship.moving_left=True
    elif event.key==pg.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pg.K_q:
        sys.exit()

def check_keyup_events (event,ship):
    """响应按键"""
    if event.key==pg.K_RIGHT:
        ship.moving_right=False
    elif event.key==pg.K_LEFT:
        ship.moving_left=False

def check_events (ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

        elif event.type==pg.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pg.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新图像"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #让最近绘制的屏幕可见
    pg.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets)<ai_settings.bullet_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def get_number_alien_x(ai_settings,alien_width):
    """计算一行可容纳多少外星人"""
    avaiable_space_x=ai_settings.screen_width-2*alien_width
    number_alien_x=int(avaiable_space_x/(2*alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    avaiable_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(avaiable_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少外星人
    alien=Alien(ai_settings,screen)
    number_alien_x=get_number_alien_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows): 
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
            