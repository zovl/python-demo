#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# Hello Python
def io_input_raw():
    str = raw_input("请输入：");
    print "你输入的内容是: ", str

# [x*5 for x in range(2,10,2)]
def io_inout():
    str = input("请输入：");
    print "你输入的内容是: ", str


# io_input_raw()
# io_inout()


# 打开一个文件
def file_open():
    f = open("file.txt", "wb")
    print "文件名: ", f.name
    print "是否已关闭 : ", f.closed
    print "访问模式 : ", f.mode
    print "末尾是否强制加空格 : ", f.softspace
    print f.isatty()
    print f.encoding
    print f.fileno()
    f.close()


# 写入文件
def file_write():
    f = open("file.txt", "wb")
    f.write("写入字符串：Hello Python！\n")
    f.write("写入字符串：Go ahead！\n")
    f.write("写入字符串：What the fuck！\n")
    f.close()


# 读取文件
def file_read():
    f = open("file.txt", "r+")
    # str = f.read()
    str = f.read(12)
    print "读取字符串：" + str
    f.close()


def file_seek():
    # 打开一个文件
    f = open("file.txt", "r+")
    str = f.read(12)
    print "读取的字符串是 : ", str

    # 查找当前位置
    position = f.tell()
    print "当前文件位置 : ", position

    # 把指针再次重新定位到文件开头
    position = f.seek(0, 6)
    print "重新定位文件位置 : ", position
    str = f.read(12)
    print "重新读取字符串 : ", str
    # 关闭打开的文件
    f.close()


def file_rename():
    # 重命名文件
    os.rename("src.txt", "dst.txt")


def file_remove():
    # 删除文件
    os.remove("dst.txt")


def file_mkdir():
    # 创建目录
    os.mkdir("catolog")


def file_rmdir():
    # 删除目录
    os.rmdir("catolog")


def file_chdir():
    # 改变当前的目录
    os.chdir("newdir")


def file_getcwd():
    # 给出当前的目录
    print os.getcwd()


file_open()
# file_write()
# file_read()
# file_seek()
# file_rename()
# file_remove()
# file_mkdir()
# file_chdir()
# file_getcwd()
# file_rmdir()