#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,re,math
import pygame as pg

def run_game ():
	#��ʼ����Ϸ������һ����Ļ����
	pg.init()
	screen = pg.display.set_mode((1280,720))
	pg.display.set_caption("Alien Invasion")
	#���ñ���ɫ
	bg_color=(230,230,230)
	
	#��ʼ��Ϸ��ѭ��
	while True:
		#���Ӽ��̺�����¼�
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
		
		#ÿ��ѭ�����ػ���Ļ
		screen.fill(bg_color)
		
		#��������Ƶ���Ļ�ɼ�
		pg.display.flip()
		
run_game()
