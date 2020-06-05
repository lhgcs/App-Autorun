#!/usr/bin/env python3

'''
@Description: 通过adb命令实现自动化
@Version: 1.0
@Autor: lhgcs
@Date: 2020-06-05 22:42:25
@LastEditors: lhgcs
@LastEditTime: 2020-06-05 22:44:23
@FilePath: /App-Autorun/main.py
'''

# pip install pillow

import os

'''
@description: 执行adb命令
@param {type} 
@return: 
'''
def adb_cmd(cmd):
    print(cmd)
    os.system(cmd)

'''
@description: 获取手机截图
@param {type} 
@return: 
'''
def get_image():
    cmd = "adb shell screencap -p /sdcard/temp.png"
    adb_cmd(cmd)

'''
@description: 获取坐标
@param {type} 
@return: 
'''
def get_position():
    image = Image.open("temp.png")
    if(image.getpixel((x, y)) == (255,255,255,255)):
        return True

'''
@description: 点击
@param {type} 
@return: 
'''
def click(x,y):
    cmd = "adb shell input tap {} {}".format(x,y)
    adb_cmd(cmd)

'''
@description: 滑动
@param {type} 
@return: 
'''
def slide(startX, startY, endX,endY):
    cmd = "adb shell input swipe {} {} {} {}".format(startX, startY, endX,endY)
    adb_cmd(cmd)

'''
@description: 输入
@param {type} 
@return: 
'''
def set_input(txt):
    cmd = "adb shell am broadcast -a ADB_INPUT_TEXT --es ms {}".format(txt)
    adb_cmd(cmd)

if __name__ == "__main__":
    pass