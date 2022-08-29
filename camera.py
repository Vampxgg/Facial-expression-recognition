import cv2
import dlib
import math
import numpy as np
import Face_recognition_model


class photo_fix():

    def show_img(img):
        cv2.imshow('1', img)

    def add_text(img):
        img_put = cv2.putText(img, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
        return img_put

    def add_shape(img):
        img_tang = cv2.rectangle(img, (20, 20), (80, 80), (242, 156, 177))
        # 画矩形
        return img_tang

    def trans_grey(img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 转灰度图
        return img_gray

    def add_circle(img):
        img_circle = cv2.circle(img, (10, 10), 2, (178, 34, 34), 5)
        # 画圆（圆心，半径，颜色，线条粗细）
        return img_circle

    def flip(img, angle=-1):
        img_flip = cv2.flip(img, angle)
        # 翻转
        return img_flip

    def resize(img, dsize=(50, 50)):
        '''
        # 这个方法是 用来翻转照片的
        ：@param_img:
        ：@param_dsize:
        '''
        img_resize = cv2.resize(img, dsize)
        return img_resize


def run():
    # 初始化ing
    # predictor_path = '../../人工智能/shape_predictor_81_face_landmarks-master/shape_predictor_81_face_landmarks.dat'
    # pre_path = './landmask/shape_predictor_5_face_landmarks.dat'
    pre_path_double = './landmask/shape_predictor_68_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(pre_path_double)

    line_brow_x = []
    line_brow_y = []

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        flag, frame = cap.read()
        if not flag:
            print('未获取到图像')
        img_flip = cv2.flip(frame, 1)
        img_gray = cv2.cvtColor(img_flip, cv2.COLOR_RGB2GRAY)

        # cv2.waitKey(0)
        faces = detector(frame, 0)
        for face in faces:
            pass

            shape = predictor(img_gray, face)
            # 8.3 获取关键点坐标
            # for pt in shape.parts():
            #     # 每个点的坐标
            #     pt_position = (pt.x, pt.y)
            #     # 绘制关键点
            #     img_set2=cv2.circle(frame, pt_position, 3, (255, 0, 0), -1)
            #     cv2.imshow('2',img_set2)
            #     img2 = frame[face.top():face.bottom(), face.left():face.right()]
            #     # cv2.imwrite("./output",img2)
            data_list = []
            # 嘴巴张开程度
            a = ((shape.part(60).x - shape.part(67).x) ** 2 + (shape.part(60).y - shape.part(67).y) ** 2) ** 0.5
            b = ((shape.part(60).x - shape.part(61).x) ** 2 + (shape.part(60).y - shape.part(61).y) ** 2) ** 0.5
            c = ((shape.part(61).x - shape.part(67).x) ** 2 + (shape.part(61).y - shape.part(67).y) ** 2) ** 0.5
            angle = round(math.acos((a * a + b * b - c * c) / (2 * a * b)) * 180 / math.pi, 1)
            print(angle)
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
            print(brow_width, brow_hight)
            data_list.append(brow_hight)
            data_list.append(brow_width)
            # print("眉毛高度与识别框高度之比：",round(brow_arv/self.face_width,3))
            # print("眉毛间距与识别框高度之比：",round(frown_arv/self.face_width,3))

            # 眼睛睁开程度
            eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y +
                       shape.part(47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
            eye_hight = (eye_sum / 4) / face_width
            print(eye_hight)
            data_list.append(eye_hight)
            # print("眼睛睁开距离与识别框高度之比：",round(eye_open/self.face_width,3))

            def get_emo(re_emo):
                cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 255), 2)
                cv2.putText(frame, re_emo, (face.left(), face.top()), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 20), 2)
                cv2.imshow('人脸识别中......', frame)

            # print(Data_characteristics)
            print(data_list)
            model = Face_recognition_model.get_model()
            re_emo = model.match(data_list)
            get_emo(re_emo)
            # print(re_emo)

        key = cv2.waitKey(10)
        if key == 32:
            cv2.waitKey(0)
            continue
        if key == 27:
            break
    # 释放摄像头
    cap.release()
    # 结束所有窗口
    cv2.destroyAllWindows()
