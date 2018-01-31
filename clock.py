# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pygame
import time
import random
import math
from time import strftime, localtime
from screen import screen
from pygame.locals import *

screen = screen()
pygame.mouse.set_visible(0)
font = pygame.font.Font('segoeui.ttf', 73)
bkgcolor = (70, 70, 70)
fgcolor = (255, 255, 255)
buffer = 50
circleY = 580
circleRadius = 5
dots = 30

def dw(texts, ons, y):
    rs = []
    totalwidth = 0
    for (i, text) in enumerate(texts):
        r = font.render(text, True, bkgcolor)
        rs.append(r)
        totalwidth += r.get_width()
    leftover = (1024 - totalwidth - (buffer * 2)) / len(texts)
    offset = buffer
    for (i, r) in enumerate(rs):
        screen.scr.blit(r, (offset, y))
        if(ons[i] == 1):
            screen.scr.blit(font.render(texts[i], True, fgcolor), (offset, y))
        offset += r.get_width() + leftover
def drawDotLine():
    second = ((int(strftime("%M", localtime())) % 5) *60) + (int(strftime("%S", localtime())))
    circleSpace = (1024 - (buffer * 2)) / (dots - 1)
    offset = buffer
    for x in range(0, dots):
        if(second / (300 / dots) >= x):
            pygame.draw.circle(screen.scr, fgcolor, (offset, circleY), circleRadius, 0)
        else:
            pygame.draw.circle(screen.scr, bkgcolor, (offset, circleY), circleRadius, 0)
        offset += circleSpace
running = True
while running:
    screen.scr.fill((0,0,0))
    line1 = 10
    line2 = 100
    line3 = 190
    line4 = 280
    line5 = 370
    line6 = 460
    hour = int(strftime("%I", localtime()))
    minute = int(strftime("%M", localtime()))
    if(minute >= 25):
        hour = (1 if hour == 12 else hour + 1)
    dw(["Es", "ist", "halb", "zehn"], [1,1,(1 if minute >= 30 and minute < 35 else 0),
        (1 if (minute >= 10 and minute < 15) or (minute >=50 and minute < 55) else 0)], line1)
    dw(["viertel","fünf", "zwanzig", "vor" ], [
        (1 if minute >= 15 and minute < 20 or minute >= 45 and minute < 50 else 0),
        (1 if minute >= 5 and minute < 10 or minute >= 25 and minute < 30 or minute >= 35 and minute < 40 or minute >= 55 else 0),
        (1 if minute >= 20 and minute < 25 or minute >= 40 and minute < 45 else 0),
        (1 if minute >= 25 and minute < 30 else 0)], line2)
    dw(["nach", "halb", "vor", "eins"], [
        (1 if minute < 25 and minute >= 5 or minute >= 35 and minute < 40  else 0),
        (1 if minute >= 25 and minute < 30 or minute >= 35 and minute < 40 else 0),
        (1 if minute >=40 else 0),
        (1 if hour == 1 else 0)], line3)
    dw(["drei", "zwei", "vier", "fünf"], [
        (1 if hour == 3 else 0),
        (1 if hour == 2 else 0),
        (1 if hour == 4 else 0),
        (1 if hour == 5 else 0)], line4)
    dw(["sechs", "sieben", "acht", "neun"], [
        (1 if hour == 6 else 0),
        (1 if hour == 7 else 0),
        (1 if hour == 8 else 0),
        (1 if hour == 9 else 0)], line5)
    dw(["zehn", "elf", "zwölf", "uhr"], [
        (1 if hour == 10 else 0),
        (1 if hour == 11 else 0),
        (1 if hour == 12 else 0),
        (1 if minute >= 0 and minute < 5 else 0)], line6)
    drawDotLine()
    pygame.display.update()
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
pygame.quit()
