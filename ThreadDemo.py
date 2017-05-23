# coding=utf-8
import thread, threading
import time

#
# def thread_run(delay):
#     while True:
#         time.sleep(delay)
#         print "hello ", time.time()
#
#
# try:
#     thread.start_new_thread(thread_run, (1,))
# except:
#     print "执行线程过程中出现了一些错误！"


# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         thread.allocate()
#         count += 1
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#
#
# # 创建两个线程
# try:
#     thread.start_new_thread(print_time("Thread-1", 2))
#     thread.start_new_thread(print_time("Thread-2", 4))
# except:
#     print "Error: unable to start thread"

lock = threading.Lock()  # 创建一低级锁，用于线程同步


class MyThread(threading.Thread):
    global num  # 声明一个全局变量

    def __init__(self, threadName, count):
        super(MyThread, self).__init__()  # 执行一下父类的构造函数
        self.threadName = threadName
        self.count = count

    def run(self):  # 重写这个方法很重要，线程跑的语句就在这个里面
        if lock.acquire(2):  # 尝试获得锁，超时等待2s。如果成功获得锁返回True。
            while self.count < 5:
                time.sleep(1)  # 使线程睡眠1s
                content = "%s, count = %d" % (self.threadName, self.count)
                print content
                self.count += 1
            if lock.locked():  # 判断锁是否处于锁定状态
                lock.release()  # 释放锁


def test():
    for i in range(5):
        name = "Thread-%d" % i
        thr = MyThread(name, 0)
        thr.start()  # 开始线程


if __name__ == "__main__":
    test()
