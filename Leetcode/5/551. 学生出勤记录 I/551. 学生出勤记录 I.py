# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:07:04 2021

@author: 11200
"""


def checkRecor(s):
    print(s.count("A"))
    print(s.count("LLL"))
    if s.count("A") < 2 and s.count("LLL") <= 0:
        return True
    else:
        return False


print(checkRecor(s="PPALLP"))
