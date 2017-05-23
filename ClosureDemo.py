# coding=utf-8
def closureFun1():
    print "closureFun1"


mClosureFun1 = closureFun1  # 将函数对象赋值给变量mClosureFun1
print mClosureFun1
mClosureFun1()


def closureFun2(arg1, arg2):
    var = 15  # 局部变量

    def innerFun(arg3):
        return arg1 + arg2 + var + arg3

    return innerFun  # 返回一个innerFun函数对象


var = 10
mInnerFun1 = closureFun2(5, 6)  # 获得一个innerFun函数对象
mInnerFun2 = closureFun2(5, 6)
print mInnerFun1(7)
print mInnerFun1 is mInnerFun2
