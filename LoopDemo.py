# coding=utf-8
s = "asdfasdjhfjkasdf"
for (index, char) in enumerate(s):  # enumerat()每次循环会取出一个len为2Tuple，包含了序列号和值。
    print "%d = %s" % (index, char)

print "\n__________________________"

languages = ("Java", "Python", "C", "C++", "C#", "Ruby", "Go")
for (position, value) in enumerate(languages):
    print "%s = %s" % (position, value)

print "\n__________________________"


def gen():
    a = 10
    yield a
    b = "hello"
    yield b
    c = (1, 3, 5, 7, 9)
    yield c

for i in gen():
    print i

print "\n__________________________"

def gen2():
    for i in range(5):
        yield i

l = (i for i in range(5))
for i in l:
    print  i

print "\n__________________________"


L = []
for i in range(3):
    L.append(i**2)

L2 = [i**2 for i in range(3)] # 使用推导式来生成表。效果和上面的循环是一样的。
# 推导式和生成器表达式很相似，就是一个是[]号，一个是()
print L
print L2

print "\n__________________________"
