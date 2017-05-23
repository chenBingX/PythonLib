# coding=utf-8
import pickle


class Hero:
    def getName(self):
        print "剑圣"


with open("/Users/chenbing/Desktop/Hero.hro", "w") as f:
    hero = Hero()
    pickle.dump(hero, f)            # 将对象转换成文本流，并储存在指定文件中

with open("/Users/chenbing/Desktop/Hero.hro", "r") as f:
    hero = pickle.load(f)           # 从指定文件重建对象
    hero.getName()