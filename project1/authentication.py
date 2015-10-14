#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""This module provides functions for authenticating users. """

def login(username, password):
    try:
        user_file = open('/home/zhangyi/repos/project1/users.txt')
        user_buf = user_file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        if [username, password] in users:
            return True
        else:
            return False
    except Exception, exc:
        print "I can't anthenticate you."
        return False

def logout():
    print '这行不会被测试用例覆盖到'
    print '这行不会被测试用例覆盖到'
