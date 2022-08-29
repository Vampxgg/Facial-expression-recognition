# -*- codeing=utf-8 -*-  
# .@FileName:'Colorful_painting'
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/8/26 11:33'
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
from tkinter import filedialog

class colorful():

    def start(self):
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.path=filedialog.asksaveasfilename(defaultextension='.png')
        self.frame_Count = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

    def getImage(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            if self.retval == True:
                self.showImage()
            else:
                break
             # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def getgray(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.imageGray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # 灰度
            if self.retval == True:
                self.showImage()
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def getThermal(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.imageTherml = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # 转到HSV色彩空间
            if self.retval == True:
                self.showImageThermal()
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def getBlackwhite(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.imageGray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # 灰度
            self.Blackwhite = cv2.threshold(self.imageGray, 127, 255, cv2.THRESH_BINARY)  # 二值化处理
            if self.retval == True:
                self.showImageBlackwhite()
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def getTwist(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.imageTwist = cv2.Canny(self.image, 10, 50)  # 阈值为10-50的Canny边缘检测
            if self.retval == True:
                self.showImageTwist()
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def getSketch(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.imageSketch = cv2.Canny(self.image, 200, 400)  # 阈值为200-400的Canny边缘检测
            if self.retval == True:
                self.showImageSketch()
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def showImage(self):
        cv2.imshow("自拍一张", self.image)
        cv2.imwrite(self.path, self.image)

    def showImageGray(self):
        cv2.imshow("灰度图", self.imageGray)
        cv2.imwrite(self.path, self.imageGray)

    def showImageThermal(self):
        cv2.imshow("热成像", self.imageTherml)
        cv2.imwrite(self.path, self.imageTherml)

    def showImageBlackwhite(self):
        cv2.imshow("黑白底片", self.Blackwhite)
        cv2.imwrite(self.path, self.Blackwhite)

    def showImageTwist(self):
        cv2.imshow("麻花照", self.imageTwist)
        cv2.imwrite(self.path, self.imageTwist)

    def showImageSketch(self):
        cv2.imshow("素描", self.imageSketch)
        cv2.imwrite(self.path, self.imageSketch)

    def add_text(self,meng):
        self.meng=meng
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.img_put = cv2.putText(self.image,self.meng, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                       (255, 0, 0))
            if self.retval == True:
                cv2.imshow("加文字", self.img_put)
                cv2.imwrite(self.path, self.img_put)
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def flip(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.img_flip = cv2.flip(self.image, angle=1)
            if self.retval == True:
                cv2.imshow("镜像", self.img_flip)

                cv2.imwrite(self.path, self.img_flip)
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def add_circle(self):
        self.start()
        i = 0
        # detector = dlib.get_frontal_face_detector()
        while (self.video.isOpened()):
            self.retval, self.image = self.video.read()  # 原图像
            self.img_circle = cv2.circle(self.image, (10, 10), 2, (178, 34, 34), 5)
            if self.retval == True:
                # 画圆（圆心，半径，颜色，线条粗细）
                cv2.imshow("画圆", self.img_circle)
                cv2.imwrite(self.path, self.img_circle)
            else:
                break
            # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
            key = cv2.waitKey(10)
            if key == 32:
                cv2.waitKey(0)
                continue
            if key == 27:
                self.close()
            i += 1
            if i == self.frame_Count:
                self.close()

    def resize(img, dsize=(50, 50)):
        img_resize = cv2.resize(img, dsize)
        return img_resize

    def add_shape(img):
        img_tang = cv2.rectangle(img, (20, 20), (80, 80), (242, 156, 177))
        # 画矩形
        return img_tang

    def close(self):
        # 释放摄像头
        self.video.release()
        # # 结束所有窗口
        cv2.destroyAllWindows()
