﻿# coding:utf-8

'''
# 列表、元组访问规则同访问字符串下标完全一致(可正向、反向、切片)
# 列表[]:list
a = [9, 7, 4, 5, 6, 3]
b = [7, 9, 'nice', [6, 8], 0]      # 对于列表来说，里面可以存储不同类型，合法
print(a[1])   # 列表、元组访问规则同访问字符串下标完全一致(可正向、反向、切片)
print(a[-1])
print(a[1:3])
a[0] = 8      # 对于列表来说，还可借助[]进行修改
print(a)
print(b)


# 元组(tuple)
# 元组与列表非常的相似，但是，列表是可变的对象，元组是不可变对象
a = (9, 6, 4, 'yes', (2, 6), 9)
# a[0] = 0   # 元组与列表非常的相似，但是，列表是可变的对象，元组是不可变对象。不可对元组进行修改
print(a)


# 整数在Python中依然是不可变类型，虽然下面运行后不报错，但是不是更改，是创建一个新的20对象，让a和20关联在一起，并非修改a,而是重新建立关联关系
# 字符串也是不可变类型，道理同整数(int)
a = 10
a = 11


# 字典{}:同C++中的map,JAVA中的hashmap，是一个键值对这样的结构;字典底层实现是哈希表
a = {
    'ip': '127.0.0.1',   # 环回ip:自己访问自己，不论电脑的ip是什么，都可以用该特定的ip表示自身，通常用于测试（网络上先完成自我测试，然后再进行跨主机测试）
}    # 创建字典
print(a['ip'])    # 取字典中的元素
a['port'] = 80    # 插入新键值对
print(a)


# 理解“引用”
a = "nice"
b = a
print(b)
print(id(a))    # 查看一个变量的身份标识（仅仅是一个标识，与内存无关），可近似看做是地址；但是地址，一方面是身份的标识，另一方面也表示变量在内存中存在的位置
print(id(b))    # 比较两个变量的值是否相同，直接用==；比较两个变量的值是否是同一个对象，可通过id()的方式进行比较
print(id(a)==id(b))
'''