# coding=utf-8
from Tkinter import *
import os


def sure():
    global path
    path = path_entry.get()
    global suffix
    suffix = suffix_entry.get()
    change_name()


def change_name():
    os.chdir(path)
    for file in os.listdir(path):
        if file.rfind(suffix) != -1:
            print 'before: ' + file
            old_name = file
            start_index = file.rindex(suffix[0])
            end_index = start_index + len(suffix)
            # print end_index
            file_length = len(file)
            # print file_length
            end_content = file[end_index:file_length]
            # print end_content
            start_content = file[0:start_index]
            new_name = start_content + end_content
            print '   after: ' + new_name
            os.rename(old_name, new_name)


root_view = Tk()
root_view.title('Delete Suffix')
root_view.geometry("300x100")  # 是字母x，不是*！

path_label = Label(root_view, text='路径')
path_label.grid(row=0)

path_entry = Entry(root_view)
path_entry.grid(row=0, column=1)

suffix_label = Label(root_view, text='需要删除的字符')
suffix_label.grid(row=1)

suffix_entry = Entry(root_view)
suffix_entry.grid(row=1, column=1)

btn = Button(root_view, text='Sure', command=sure)
btn.grid(row=2, column=1)

root_view.mainloop()
