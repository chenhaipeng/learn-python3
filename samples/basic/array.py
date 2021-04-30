#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python的二维数组操作 https://blog.csdn.net/qq_24504591/article/details/88222491
arr = [[] for i in range(5)]
arr[0] = 1
print (arr)
# >>> [[], [], [], [], []]
arr1 = [[0, 0] for i in range(5)]
arr1[1][1] = 1
# >>> [[0, 0], [0, 0], [0, 0, 2], [0, 0], [0, 0]]
print (arr1)

arr2 = [[0, 0]] * 2
arr2[1][1] = 1
print (arr2)
