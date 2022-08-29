# -*- codeing=utf-8 -*-  
# .@FileName:'Face recognition model'
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/8/25 15:52'
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

import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import csv


class get_model():
    def run_knn(self, data_list):
        ktest = joblib.load('./Identify the model/knn.pkl')
        lis = [data_list]
        index = ktest.predict(lis)
        emotion = ['argry', 'happy', 'normol', 'sadness']
        # print(emotion[int(index)])
        re_emo = emotion[int(index)]
        return re_emo

    def run_facenet(self, data_list):
        pass

    def run_svm(self, data_list):
        pass

    def run_kears(self, data_list):
        ktest = joblib.load('./Identify the model/facenet_mobilenet.pth')
        lis = [data_list]
        index = ktest.predict(lis)
        emotion = ['argry', 'happy', 'normol', 'sadness']
        # print(emotion[int(index)])
        re_emo = emotion[int(index)]
        return re_emo

    def match(self,data_list):
        self.data_list = data_list
        with open('./Identify the model/model.txt','r')as f:
            model = f.read()
            # 字符串前缀，后缀匹配
            filename = str(model)
            a = filename.startswith('knn')  # 前缀匹配
            b = filename.startswith('facenet')  # 前缀匹配
            c = filename.startswith('svm')  # 前缀匹配
            d = filename.startswith('kears')  # 前缀匹配
            # print(a, b, c, d)
            if a:
                re=self.run_knn(self.data_list)
                return re
            elif b:
                re=self.run_facenet(self.data_list)
                return re
            elif c:
                re=self.run_svm(self.data_list)
                return re
            else:
                re=self.run_kears(self.data_list)
                return re


def getModel(word):
    model = word
    with open('./Identify the model/model.txt','w+')as f:
        f.write(model)
        f.close()