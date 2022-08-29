# -*- codeing=utf-8 -*-  
# .@FileName:'cv_video'
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/6/30 9:35'
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


video = cv2.VideoCapture("D:/Above the Clouds.mp4")

frame_Count = video.get(cv2.CAP_PROP_FRAME_COUNT)
i = 0
while (video.isOpened()):
    retval, image1 = video.read()  # 原图像
    image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 灰度
    image3 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)  # 转到HSV色彩空间
    t4, image4 = cv2.threshold(image2, 127, 255, cv2.THRESH_TOZERO)  # 低于阈值零处理
    t5, image5 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)  # 二值化处理
    image6 = cv2.Canny(image1, 10, 50)  # 阈值为10-50的Canny边缘检测
    image7 = cv2.Canny(image1, 200, 400)  # 阈值为200-400的Canny边缘检测
    # 设置“Video”窗口
    cv2.namedWindow("playing_basketball_1", 0)
    cv2.resizeWindow("playing_basketball_1", 426, 240)
    cv2.namedWindow("playing_basketball_2", 0)
    cv2.resizeWindow("playing_basketball_2", 426, 240)
    cv2.namedWindow("playing_basketball_3", 0)
    cv2.resizeWindow("playing_basketball_3", 426, 240)
    cv2.namedWindow("playing_basketball_4", 0)
    cv2.resizeWindow("playing_basketball_4", 426, 240)
    cv2.namedWindow("playing_basketball_5", 0)
    cv2.resizeWindow("playing_basketball_5", 426, 240)
    cv2.namedWindow("playing_basketball_6", 0)
    cv2.resizeWindow("playing_basketball_6", 426, 240)
    cv2.namedWindow("playing_basketball_7", 0)
    cv2.resizeWindow("playing_basketball_7", 426, 240)
    if retval == True:
        cv2.imshow("playing_basketball_1", image1)
        cv2.imshow("playing_basketball_2", image2)
        cv2.imshow("playing_basketball_3", image3)
        cv2.imshow("playing_basketball_4", image4)
        cv2.imshow("playing_basketball_5", image5)
        cv2.imshow("playing_basketball_6", image6)
        cv2.imshow("playing_basketball_7", image7)
        cv2.imwrite('./outut/sex.png',image7)
    else:
        break
    # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
    key = cv2.waitKey(10)
    if key == 32:
        cv2.waitKey(0)
        continue
    if key == 27:
        break
    i += 1
    if i == frame_Count:
        break


video.release()
cv2.destroyAllWindows()
