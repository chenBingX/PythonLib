# coding=utf-8

if True:
    print "你好，世界!"
    print "你好，世界!"
else:
    print "Hello World!"

# raw_input("asdasd")

str1 = "abcdefg"
print str1[1:3]
print str1[5]

str3 = str1 * 3
print str3

num1 = 2
num2 = 3
num3 = num1 * num2
print num3

list = ["hello world", 798, 100.1, "Hello"]
print list
list2 = list[1:3]
print list2

list3 = list + list2
print list3

dict = {2: "2", "1": "HELLO", 0.15: "WORLD"}
print dict[0.15]

str4 = str(num1)
print str4

a = True
b = 20
print a and b

list4 = ["hello", "2", 5, 20]
print b in list4

list5 = ["hello", "2", 5, 10]
print b not in list5

class Obj:
    def __init__(self, a):
        self.var = a

c = Obj(1)
d = Obj(1)
print id(c)
print id(d)

e = 0.25
f = 0.25
print e is f

def printModelName():
    print "Demo.py"


def printModelName2():
    print "2 - Demo.py"





