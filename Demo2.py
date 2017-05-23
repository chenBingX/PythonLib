# coding=utf-8
# count = 0
# while count < 9:
#     print "当前count = ", count
#     count += 1

for index in range(0, 10):
    print "当前index = ", index

for char in "Python":
    print "当前char = ", char

for mClass in ["数学", "语文", "英语"]:
    print "当前Class = ", mClass

print "\n质数就是只有1和该数本身两个因数的数"
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print "%d = %d * %d" % (num, i, j)
            break
    else:
        print num, "是一个质数"

for i in range(0, 10):
    if i == 5:
        pass
        print "pass"
    print "i = ", i

var1 = "hello world"
var1 = var1[:6] + "WORLD"
print var1

import calendar

cal = calendar.month(2016, 1)
print "\n", cal

def sayHello(content):
    print "\nHello"

sayHello("asdfasdf")

def printInfo(arg1, *vartuple):
    print arg1
    for var in vartuple:
        print var
printInfo("\na","b","c","d",1)

def msum(var1, var2):
    return var1 + var2
sumresult = msum(1,1)
print "\n",sumresult

def changeVar(var):
    var = "0"
var2 = "hello"
changeVar(var2)
print "var2 = %s" % var2

def changeObj(obj):
    obj.append([1,2,3])
mylist = [5,6,7]
changeObj(mylist)
print mylist

def writeCode(logic1, logic2):
    print "logic1 = %s, logic2 = %s" % (logic1, logic2)
writeCode(logic2 = "world", logic1 = "hello")

def printDefualtVar(var = "hello"):
    print "\n", var
printDefualtVar()

def returnFoo():
    return "return"
strReturn = returnFoo()
print "\n", strReturn

from Demo import printModelName2
printModelName2()

import Demo
Demo.printModelName()

content = dir(Demo)
print "\n", content

input_content = raw_input("请输入：")
print "你输入的内容是：",input_content

