'''
    1602/1602A
    author：ZengXiaojie
    description：
        直接实例化 My1602 对象
        然后调用对象的 print_lcd(param1, param2, str) 方法
            ex：print_lcd(0, 0, 'Hello, world!')
            param1：从第几位开始，共16位（0-15），超出不显示，除非移动屏幕（其实1602一行有40位）
            param2：第几行，共有两行，0为第一行，1位第二行。
            str：要显示的数据
        每次打印字符时，建议适当清屏。
'''

import time
import smbus2
import sys

class My1602(object):
    BUS = smbus2.smbus2(1)
    LCD_ADDR = 0x27
    BLEN = 1

    # '''
    # 开关灯
    def turn_light(self, key):
        self.BLEN = key
        if key == 1:
            self.BUS.write_byte(self.LCD_ADDR, 0x08)
        else:
            self.BUS.write_byte(self.LCD_ADDR, 0x00)
    # '''

    def write_word(self, addr, data):
        temp = data
        if self.BLEN == 1:
            temp |= 0x08
        else:
            temp &= 0xF7
        self.BUS.write_byte(addr, temp)

	# 写命令
    def send_command(self, comm):
        # 发送7-4位数据
        buf = comm & 0xF0
        buf |= 0x04  # RS = 0, RW = 0, EN = 1
        self.write_word(self.LCD_ADDR, buf)
        time.sleep(0.002)
        buf &= 0xFB
        self.write_word(self.LCD_ADDR, buf)

        # 发送3-0位数据
        buf = (comm & 0x0F) << 4
        buf |= 0x04  # RS = 0, RW = 0, EN = 1
        self.write_word(self.LCD_ADDR, buf)
        time.sleep(0.002)
        buf &= 0xFB
        self.write_word(self.LCD_ADDR, buf)

	# 写数据
    def send_data(self, data):
        # 发送7-4位数据
        buf = data & 0xF0
        buf |= 0x05  # RS = 1, RW = 0, EN = 1
        self.write_word(self.LCD_ADDR, buf)
        time.sleep(0.002)
        buf &= 0xFB
        self.write_word(self.LCD_ADDR, buf)

        # 发送3-0位数据
        buf = (data & 0x0F) << 4
        buf |= 0x05  # RS = 1, RW = 0, EN = 1
        self.write_word(self.LCD_ADDR, buf)
        time.sleep(0.002)
        buf &= 0xFB
        self.write_word(self.LCD_ADDR, buf)
	
	# 初始化
    def __init__(self):
        try:
            self.send_command(0x33)
            time.sleep(0.005)
            self.send_command(0x32)
            time.sleep(0.005)
            self.send_command(0x28)
            time.sleep(0.005)
            self.send_command(0x0C)
            time.sleep(0.005)
            self.send_command(0x01)
            self.BUS.write_byte(self.LCD_ADDR, 0x08)
        except:
            return None
        else:
            return None

	# 清屏
    def clear_lcd(self):
        self.send_command(0x01)  # 清屏

	# 显示字符
    def print_lcd(self, x, y, str):
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y < 0:
            y = 0
        if y > 1:
            y = 1

        addr = 0x80 + 0x40 * y + x
        self.send_command(addr)

        for chr in str:
            self.send_data(ord(chr))


if __name__ == '__main__':
    my1602 = My1602()
    # turn_light(0)  # 关闭背景灯光
    my1602.print_lcd(0, 0, 'Hello, world!')
    my1602.print_lcd(8, 1, 'by zxj')
    
