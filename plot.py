# -*- codeing=utf-8 -*-
# .@FileName:'plot'
# .@Author='_不咬闰土的猹丶'
# .@Date='2022/7/1 11:15'
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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke, Normal

class set_info():

    def making(self):
        # 解决 matplotlib 显示中文问题
        plt.rcParams['font.sans-serif'] = ['华文彩云 常规']  # 指定默认字体
        # 解决保存图像是负号 '-' 显示为方块的问题
        plt.rcParams['axes.unicode_minus'] = False

        fig = plt.figure(figsize=(10, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)
        ax.set_xticks([])
        ax.set_yticks([])
        family = "华文彩云 常规"
        size = 80
        cmap = plt.cm.Blues_r
        text = "曦fan科技"

        for x in np.linspace(0, 1, 20):
            lw, color = x * 225, cmap(1 - x)
            t = ax.text(
                0.5,
                0.45,
                text,
                size=size,
                color="none",
                weight="bold",
                va="center",
                ha="center",
                family=family,
                zorder=-lw,
            )
            t.set_path_effects([Stroke(linewidth=lw + 1, foreground="black")])
            t = ax.text(
                0.5,
                0.45,
                text,
                size=size,
                color='red',  # 中心文字颜色
                weight="bold",
                va="center",
                ha="center",
                family=family,
                zorder=-lw + 1,
            )
            t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
        t = ax.text(
            1.0,
            0.01,
            "https://vamp.hxdsg.xyz",
            va="bottom",
            ha="right",
            size=10,
            color="white",
            family="华文彩云 常规",
            alpha=0.50,
        )

        # plt.savefig("./signature.png")
        # plt.savefig("signature.pdf")
        plt.savefig("signature.png")
        plt.show()
