# coding=utf-8

'''
Created on 2016年12月22日

验证码

@author: pangt
'''
# coding=utf-8
import random
import string
import sys
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tutils.tconf import BASE_DIR, T_FAILED, T_SUCCESS
import logging
from tutils.t_log import TLog
import time
import threading
from time import sleep
from os.path import os
#from nt import rmdir, remove

# 字体的位置，不同版本的系统会有不同
font_path = BASE_DIR + '/files/ttf/sjt.ttf'
yzm_path = BASE_DIR + '\\static\\yzm\\'
# 生成几位数的验证码
number = 4
# 生成验证码图片的高度和宽度
size = (200, 60)
# 背景颜色，默认为白色
bgcolor = (255, 255, 255)
# 字体颜色，默认为蓝色
fontcolor = (0, 0, 255)
# 干扰线颜色。默认为红色
linecolor = (255, 0, 0)
# 是否要加入干扰线
draw_line = True
# 加入干扰线条数的上下限
line_number = (1, 5)
#字号
text_size = 65

class T_YZM:
    
    text = ""
    path = ""
    res = T_FAILED
    
    def __init__(self, text="", path="", res=T_FAILED):
        self.path = path
        self.text = text
        self.res = res
 
# 用来随机生成一个字符串
def gene_text():
    source =list(string.letters)
    L = []
#     L.append(range(0, 10))
#     L.append(range(97, 26))
#     source =list(L)
#     for index in range(0, 10):
#         source.append(str(index))
    res =  ''.join(random.sample(source, number)).lower()  # number是生成验证码的位数
    return res

# 用来绘制干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)
 
# 生成验证码
def gene_code():
    text = ""
    pic_name = ""
    yzm_model = T_YZM()
    try :
        width, height = size  # 宽和高
        image = Image.new('RGBA', (width, height), bgcolor)  # 创建图片
        font = ImageFont.truetype(font_path, text_size)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)
        draw.text(((width - font_width) / number, (height - font_height) / number), text,
                font=font, fill=fontcolor)  # 填充字符串
        if draw_line:
            gene_line(draw, width, height)
            gene_line(draw, width, height)
            gene_line(draw, width, height)
            
        image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.1, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
        s_time = str(int(time.time() * 100))
        pic_name = "yzm_" + s_time + ".png"
        pic_path = yzm_path + pic_name
        image.save(pic_path)  # 保存验证码图片
    except Exception as e:
        logging.exception(e)
    yzm_model = T_YZM(text, pic_name, T_SUCCESS)
    return yzm_model 


def __clear_outtime_code_func():
    """
    清除过期验证码
    """
    while(True) :
        sleep(600)
        try :
            curr_time = time.time()
            logging.debug("---清除过期验证码")
            if False == os.path.isdir(yzm_path) :
                continue
            fl = os.listdir(yzm_path)
            for f in fl :
                abs_f = yzm_path + f
                if True == os.path.isdir(abs_f) :
                    print("文件夹  " + f)
                if True == os.path.isfile(abs_f) :
                    upd_time = os.path.getmtime(abs_f)
                    if(curr_time - upd_time) > 600 :
                        print("删除文件 ： " , f , upd_time)
                        os.remove(abs_f)
                else :
                    print("err " + f)
        except Exception as e :
            logging.exception(e)

def clear_overtime_code_func():
    """
    清除过期验证码
    """
    logging.debug("---启动清除过期验证码")
    t_clear_yzm = threading.Thread(target=__clear_outtime_code_func)
    t_clear_yzm.start()
    
if __name__ == "__main__":
    TLog.init()
    print(gene_text())
#     gene_code()
#     clear_outtime_code_func()
#     while True :
#         txt , pic_path = gene_code()
#         print("生成%s , %s" % (txt, pic_path))
#         sleep(1)
