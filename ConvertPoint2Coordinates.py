# -*-coding:utf-8-*-
import time
import pyautogui as pag
import win32gui, win32ui, win32con
from PIL import Image
import pytesseract
import webbrowser


def writeCoordinates(count, x, y):
    position = str(count) + ' ' + str(x) + ' ' + str(y) + '\n'
    with open('Coordinates.txt', 'a') as f:
        f.write(position)

yscale = float(input('左上角定位,输入纵坐标最大值：'))
while True:
    if (yscale > 0):
        x1, y1 = pag.position()  # 返回鼠标的坐标
        posStr = "Position:" + str(x1).rjust(4) + ',' + str(y1).rjust(4)
        print("左上角坐标：", posStr)  # 打印坐标
        break
xscale = float(input('右下角定位,输入横坐标最大值：'))
while True:
    if (xscale > 0):
        x2, y2 = pag.position()  # 返回鼠标的坐标
        posStr = "Position:" + str(x2).rjust(4) + ',' + str(y2).rjust(4)
        print("右下角坐标：", posStr)  # 打印坐标
        break

count = 1
while True:
    i = input('按a键定位点坐标,s键退出：')
    if ('a' == i):
        pix_x, pix_y = pag.position()  # 返回鼠标的坐标
        x=xscale*(pix_x-x1)/(x2-x1)
        y=yscale*(pix_y-y2)/(y1-y2)
        posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        print("当前鼠标坐标：", posStr)  # 打印坐标
        writeCoordinates(count, x, y)
        count = count + 1
    if ('s' == i):
        exit(0)
