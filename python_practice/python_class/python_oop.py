# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 20:12
# @Author  : feier
# @File    : python_oop.py

# 面向对象
class House:
    # 静态属性->类变量（类之中，方法之外）
    door = "red"
    floor = "white"

    # 构造函数，在类实例化的时候直接执行
    def __init__(self):
        # 在方法当中调用类变量需要加上self.
        print(self.door)
        # 实例变量，类当中，方法当中，以"self.变量名"方式去定义
        self.kitchen = "cook"

    # 动态方法
    def sleep(self):
        # 普通变量：类当中，方法当中，前面没有self
        bed = "席梦思"
        self.table = "桌子可以放东西"
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):
        print(self.kitchen)
        print(self.table)
        print("在房子里可以做饭吃")


# 把类实例化
# 北欧风房子
north_house = House()
# 中式风房子
china_house = House()
north_house.sleep()
north_house.cook()

# north_house.sleep()
# 调用类属性
# print(House.door)
# # 修改类属性
# House.door = "white"
# print(House.door)
# # 实例对象调用类属性
# print(north_house.door)
# 修改对象属性
# north_house.door = "black"
# print(north_house.door)
# print(House.door)
# print(china_house.door)