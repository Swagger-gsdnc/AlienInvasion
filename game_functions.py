#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,re,math
import pygame as pg
from bullet import Bullet

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


def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新图像"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()        

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
    