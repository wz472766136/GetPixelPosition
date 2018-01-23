# -*-coding:utf-8-*-
import time
import pyautogui as pag
import win32gui, win32ui, win32con
from PIL import Image
import pytesseract
import webbrowser


def window_capture(filename, x1, y1, x2, y2):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    w = x2 - x1
    h = y2 - y1
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x1, y1), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


while True:
    if ('1' == input('左上角定位：')):
        x1, y1 = pag.position()  # 返回鼠标的坐标
        posStr = "Position:" + str(x1).rjust(4) + ',' + str(y1).rjust(4)
        print("左上角坐标：", posStr)  # 打印坐标
        break
while True:
    if ('2' == input('右下角定位：')):
        x2, y2 = pag.position()  # 返回鼠标的坐标
        posStr = "Position:" + str(x2).rjust(4) + ',' + str(y2).rjust(4)
        print("右下角坐标：", posStr)  # 打印坐标
        break
count = 1
while True:
    if (input('按任意键回车搜题：')):
        start = time.time()
        filename = 'question' + str(count) + '.jpg'
        count = count + 1
        window_capture(filename, x1, y1, x2, y2)
        im = Image.open(filename, 'r')
        Lim = im.convert('L')
        text = pytesseract.image_to_string(Lim, lang='chi_sim')
        new_text = ''.join(text.split())
        print(new_text)
        url = 'http://www.baidu.com/s?wd=%s' % new_text
        webbrowser.open(url)
        end = time.time()
        print(end - start)
