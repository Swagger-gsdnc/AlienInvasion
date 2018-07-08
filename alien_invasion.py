#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,re,math
import pygame as pg

def run_game ():
	#初始化游戏并创建一个屏幕对象
	pg.init()
	screen = pg.display.set_mode((1280,720))
	pg.display.set_caption("Alien Invasion")
	#设置背景色
	bg_color=(230,230,230)
	
	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
		
		#每次循环都重绘屏幕
		screen.fill(bg_color)
		
		#让最近绘制的屏幕可见
		pg.display.flip()
		
run_game()
