# coding=utf-8
import os
root_path = "/Users/chenbing/Downloads/【UI】个人主页优化/profile_icon"
del_suffix = "@2x.png"
os.chdir(root_path)
for file in os.listdir(root_path):
    if file.rfind(del_suffix) != -1:
        print "改名前：" + file
        old_name = file
        start_index = file.rindex(del_suffix[0])
        end_index = start_index + len(del_suffix)
        # print end_index
        file_length = len(file)
        # print file_length
        end_content = file[end_index:file_length]
        # print end_content
        start_content = file[0:start_index]
        new_name = start_content + end_content
        print "  改名后：" + new_name
        # os.rename(old_name, new_name)
