#!/usr/bin/env python
# coding=utf-8
'''
Author: Johannes Liu
LastEditors: Johannes Liu
email: iexkliu@gmail.com
github: https://github.com/johannesliu
Date: 2022-09-26 08:39:11
LastEditTime: 2022-11-10 00:49:53
motto: Still water run deep
Description: Modify here please
FilePath: \Learning_Advanced_Mathematics_with_Python\deploy.py
'''
import os

os.system("gitbook build")
os.system("git add -A")
os.system("git commit -m \"update\"")
os.system("git push")