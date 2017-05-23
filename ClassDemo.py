# coding=utf-8
class Hero:
    """
Hero类。
创建一个属于自己的英雄吧！
    """
    race = "human"                  #公开类变量。类的所有实例都会有的变量。每个实例的操作互不影响。类似Java中的静态变量。
    __conspirasy = "join orc"       #私有类变量。只能在类内部使用。类似Java的private

    def __init__(self):
        pass

    def __init__(self, name):       #构造函数，必须是__init__。并且，类中的方法的第一个参数必须是self，表示类本身。
        self.name = name            #类的属性可以用self.xxx直接生成，不需要提前定义。这种属性不能被继承。

    def attack(self, damage):
        print "%s 造成了 %d 点伤害" % (self.name, damage)

    def __del__(self):              #析构函数，在类被销毁的时候会被调用
        class_name = self.__class__.__name__  #获取类名
        print class_name, "销毁"

    def __selfFoo(self):             #私有函数，只能在类内部调用
        pass

    def do(self):
        print "\n调用Hero的do（)"


hero1 = Hero("剑圣")
hero1.attack(100)                   #调用实例的方法
print hero1.__doc__                 #获得开头的类说明文档
print hero1.__dict__                #获得类的属性
print hero1.__module__              #获得类所在模块的模块名
print Hero.__name__                 #获取类名，需要使用类名调用，不能用类的实例调用。
hero1.name = "牛头人酋长"            #类的属性相当于Java中的public成员变量，可以直接修改值
print hero1.name
del hero1.name                      #类的实例的属性也是可以删除的，删除了就相当于没有这个属性了
try:
    print hero1.name
except Exception:
    print "Hero1的name属性已经被删除"
else:
    print "Hero1的name属性并没有被删除"

print hero1.race
hero1.race = "orc"
print hero1.race

hero2 = Hero("伊利丹")
hero3 = Hero("娜迦")
print hero2.race
# del Hero                            #del+类名，会直接删除类的所有实例。同时会删除这个类，就相当于这个类不存在。
# hero4 = Hero()                      #此时Hero类已经被删除，执行该语句会报错。
del hero1                           #显示的删除引用


class SuperMan:
    def __init__(self):
        pass

    def do(self):
        print "\n调用SuperMan的do（)"



class SuperHero(SuperMan,Hero):
    def __init__(self):
        self.name = ""
        pass


superHero1 = SuperHero()
superHero1.do()

print hasattr(superHero1,"name")

