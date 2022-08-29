# -*- codeing=utf-8 -*-
# .@FileName:'index'
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/7/1 11:13'
# .@Email:'hx1561958968@gmail.com'

# /@Motto:'Hey guy,Did you do any coding today?'

#                '大部分人都在关注你飞的高不高，却没人在乎你飞的累不累，这就是现实！'
#                           '请不要相信梦想，只，相，信，自，己！'
# ..............................................................................................
#                            _ooOoo_
#                           o8888888o
#                           88" . "88
#                           (| -_- |)
#                            O\ = /O
#                        ____/`---'\____
#                      .   ' \\| |// `.
#                       / \\||| : |||// \
#                     / _||||| -:- |||||- \
#                       | | \\\ - /// | |
#                     | \_| ''\---/'' | |
#                     \ .-\__ `-` ___/-. /
#                   ___`. .' /--.--\ `. . __
#                ."" '< `.___\_<|>_/___.' >'"".
#               | | : `- \`.;`\ _ /`;.`/ - ` : | |
#                 \ \ `-. \_ __\ /__ _/ .-` / /
#         ======`-.____`-.___\_____/___.-`____.-'======
#                            `=---='
#
#         .............................................
#                  佛祖保佑             永无BUG
#          佛曰:
#                  写字楼里写字间，写字间里程序员；
#                  程序人员写程序，又拿程序换酒钱。
#                  酒醒只在网上坐，酒醉还来网下眠；
#                  酒醉酒醒日复日，网上网下年复年。
#                  但愿老死电脑间，不愿鞠躬老板前；
#                  奔驰宝马贵者趣，公交自行程序员。
#                  别人笑我忒疯癫，我笑自己命太贱；
#                  不见满街漂亮妹，哪个归得程序员？
#         .............................................
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
#         .............................................
import cv2
import dlib
import math
import numpy as np
import tkinter as tk
import os
from tkinter import filedialog
import Face_recognition_model
from tkinter import messagebox
import camera

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.window_sign = master
        self.filePath = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # 标签组件
        label_kuang = tk.Label(self.window_sign, text='选择目录：', font=('华文彩云', 15))
        label_kuang.place(x=250, y=420)
        label_catch = tk.Label(self.window_sign, text='打开摄像头：', font=('华文彩云', 15))
        label_catch.place(x=250, y=460)
        label_more = tk.Label(self.window_sign, text='获取更多：', font=('华文彩云', 15))
        label_more.place(x=250, y=500)

        # 输入框控件
        self.entry = tk.Entry(self.window_sign, font=('FangSong', 10), width=30, state='readonly')
        self.entry.place(x=350, y=420)
        self.entry.insert(0, "请选择文件")

        entry_catch = tk.StringVar()
        entry_cat = tk.Entry(self.window_sign, textvariable=entry_catch, font=('FangSong', 10), width=30,
                             state='readonly')
        entry_cat.place(x=350, y=460)
        entry_more = tk.StringVar()
        entry_mo = tk.Entry(self.window_sign, textvariable=entry_more, font=('FangSong', 10), width=30,
                            state='readonly')
        entry_mo.place(x=350, y=500)

        button = tk.Button(self.window_sign, text='选择路径', command=self._getFile)
        button.place(x=600, y=430)
        button_catch = tk.Button(self.window_sign, text='人脸捕获', command=camera.run)
        button_catch.place(x=600, y=470)
        self.button_ok = tk.Button(self.window_sign, text='识别', command=self.Feauture)
        self.button_ok.place(x=670, y=430)
        # if button_ok:
        #     back_ok = button_ok
        #     tk.messagebox.showerror(message=back_ok)
        # else:
        #     mess = button_ok
        #     tk.messagebox.showerror(message=mess)
        button_more = tk.Button(self.window_sign, text='更多成像', command=self.change)
        button_more.place(x=600, y=510)


    # 打开文件并显示路径
    def _getFile(self):
        default_dir = r"文件路径"
        self.filePath = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        print(self.filePath)
        self.entry.delete(0, "end")
        self.entry.insert(0, self.filePath)

def Feauture(word):
    # 人脸检测模型的路径，对象定义
    pre_path = './landmask/shape_predictor_5_face_landmarks.dat'
    pre_path_double = './landmask/shape_predictor_68_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(pre_path_double)

    # 用于测试的数据库照片的定义
    img_path = word
    line_brow_x = []
    line_brow_y = []

    '''
    用于存储数据特征的列表
    ：@prarm_label:保存图片对应人工分类的表情
    ：@prarm_label_id:将表情数字化标号分类
    ：@prarm_label_Data_characteristics:保存脸部信息的嘴巴，眉毛，眼睛的比列特征
    '''

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(img, 0)
    for face in faces:

        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 255), 2)

        shape = predictor(gray, face)
        data_list = []
        # 嘴巴张开程度
        a = ((shape.part(60).x - shape.part(67).x) ** 2 + (shape.part(60).y - shape.part(67).y) ** 2) ** 0.5
        b = ((shape.part(60).x - shape.part(61).x) ** 2 + (shape.part(60).y - shape.part(61).y) ** 2) ** 0.5
        c = ((shape.part(61).x - shape.part(67).x) ** 2 + (shape.part(61).y - shape.part(67).y) ** 2) ** 0.5
        angle = round(math.acos((a * a + b * b - c * c) / (2 * a * b)) * 180 / math.pi, 1)
        # print(angle)
        data_list.append(angle)

        # 两边眉毛距离比列占比
        brow_sum = 0
        eyebrow_sum = 0
        for j in range(17, 21):
            brow_sum += (shape.part(j).y - face.top()) + (shape.part(j + 5).y - face.top())
            eyebrow_sum += shape.part(j + 5).x - shape.part(j).x
            line_brow_x.append(shape.part(j).x)
            line_brow_y.append(shape.part(j).y)

        tempx = np.array(line_brow_x)
        tempy = np.array(line_brow_y)
        # np.ployfit(x,a,n)拟合点集a得到n级多项式，其中x为横轴长度
        z1 = np.polyfit(tempx, tempy, 1)  # 拟合成一次直线
        # round(x [,n])返回浮点数x的四舍五入值 round(80.23456, 2)返回80.23
        face_width = -round(z1[0], 3)  # 拟合出曲线的斜率和实际眉毛的倾斜方向是相反的

        brow_hight = (brow_sum / 10) / face_width  # 眉毛高度占比
        brow_width = (eyebrow_sum / 5) / face_width  # 眉毛距离占比
        # print(brow_width, brow_hight)
        data_list.append(brow_hight)
        data_list.append(brow_width)
        # print("眉毛高度与识别框高度之比：",round(brow_arv/self.face_width,3))
        # print("眉毛间距与识别框高度之比：",round(frown_arv/self.face_width,3))

        # 眼睛睁开程度
        eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y +
                   shape.part(47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
        eye_hight = (eye_sum / 4) / face_width
        # print(eye_hight)
        data_list.append(eye_hight)
        # print("眼睛睁开距离与识别框高度之比：",round(eye_open/self.face_width,3))
        if data_list:
            print(data_list)
            model = Face_recognition_model.get_model()
            re_emo = model.run_knn(data_list)
            tk.messagebox.showerror(message='这张照片的表情是' + re_emo)
            print(re_emo)
        else:
            tk.messagebox.showerror(message='请问你放入的是人脸？？')


