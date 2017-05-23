# coding=utf-8
file = open("/Users/chenbing/Desktop/博客用图/公共文案/公共文案1.md")
file_content = file.read()
print file_content
print file.name
file.close()

# file2 = open("/Users/chenbing/Desktop/Demo.md","w+")
# write_content = raw_input("请输入内容：")
# file2.write(write_content)
# file2.close()

import os

print os.getcwd()

# os.chdir("/Users/chenbing/Desktop")
# print os.getcwd()
# # os.mkdir("TestRoot")
# print os.getcwd()

# raise Exception("抛出了异常")
