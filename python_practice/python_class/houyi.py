# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 21:42
# @Author  : feier
# @File    : houyi.py
from python_practice.python_class.game_oop import Game


class HouYi(Game):
    '''
    后裔，后裔继承了Game的hp 和power。并多了护甲属性。
    重新定义另外一个defense属性：
    final_hp = hp + defense - enemy_power
    enemy_final_hp = enemy_hp - power
    两个hp进行对比，血量先为零的人输掉比赛
    '''
    # 定义护甲属性
    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        # 通过继承调用父类的构造函数，拿到父类的属性
        super().__init__(my_hp, enemy_hp)

    # 改造fight方法
    def fight(self):
        while True:
            # 修改my_hp的计算方式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)

            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


houyi = HouYi(1000, 1300)
houyi.fight()
houyi.rest(3)