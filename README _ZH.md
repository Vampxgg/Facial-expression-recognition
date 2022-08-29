## Facial expression recognition：人脸表情识别模型
---

# -*- codeing=utf-8 -*-
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/7/5 10:34'
# .@Email:'hx1561958968@gmail.com'
# /@Motto:'Hey guy,Did you do any coding today?'

#                '大部分人都在关注你飞的高不高，却没人在乎你飞的累不累，这就是现实！'
#                           '请不要相信梦想，只，相，信，自，己！'
# ..............................................................................................

## 所需环境
python==3.39.1

## 所需库
from tkinter import *
import tkinter as tk
from tkinter import ttk
from time import strftime
from tkinter import messagebox
from tkinter import filedialog
import pickle
from PIL import Image, ImageTk
import Face_recognition_model
import os
import random
import webbrowser
import camera
import Feature_extraction
import Colorful_painting

## 目录结构
|-Facial expression recognition
    |-.idea
    |-ad_img
        |-face.gif
        |-Welcome.jpg
    |-background
        |-...
    |-Data_output
        |-...
    |-icon
        |-...
    |-Identify
        |-...
    |-img_ceji
        |-...
    |-landmask
        |-...
    |-output
        |-...
    camera.py
    Colorful_painting.py
    ......

## 使用说明
运行GUI.py文件启动程序，使用里面的功能

##捐赠
支付宝扫码捐赠
![palpay.png](Facial expression recognition/icon/palpay.png)

微信支付捐赠
![wechat.png](Facial expression recognition/icon/wechat.png)