#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,re,math
import pygame as pg

def check_events ():
    """响应按键和鼠标事件"""
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

def update_screen (ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新图像"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()        

    #让最近绘制的屏幕可见
    pg.display.flip()
