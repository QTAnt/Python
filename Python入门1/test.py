# coding:utf-8
'''
# coding = utf-8
# 如果是Python2，中文注释会报错，需要加上上面其中一句即可
# print('hello world')
# import qrcode  #生成一个二维码
# qrcode.make('平凡的美好').save('./test.png')

num = 10
count = num+1

# float 相当于 Python中的 double
pi = 11.1

# 单双引号无差别
name1 = 'congcong'
name2 = "congcong"
name3 = "聪聪"
# Python是动态类型的编程语言，一个变量在创建出来之后可以在程序运行过程中类型发生改变(name在最初创建时是字符串类型，后来成int类型)
name = 100

# 变量名注意事项：数字、字母、下划线_ 三部分组成；变量名能够“见名知意”

# 多行注释时可以用 " 替换 '
'''

"""
# num = 10
# print(type(num))
# Python的 int 大小无限制，想有多大就多大
num = 1000000 * 1000000 * 1000000
print(type(num))
print(num)

# 支持复数类型
num = 10 + 5j  # 10为实部，5j为虚部（j为 -1开根号）
"""

# 字符串类型（' " 无差别，原本包含'或" 的可以岔开使用）
# 字符串前面加 r ,表示原始字符串(raw_string) 字符串内部的转义字符不生效
# My name is "congcong"
# name = "My name is 'congcong' "
# name = 'My name is "congcong" '
# name = ''' My 'name' is "congcong" '''
# name = """ My "name" '''is''' "congcong" """
# name = r"My 'name' '''is''' 'congcong' "


'''
# #取字符串下标
# 数字为正数，表示从前往后数（从0开始）；数字为负数，表示从后往前数（从-1开始）-1 => len -1
# 正取
name = "My 'name' '''is''' 'congcong' \n"
print(name[1])   # []表示要取出一位数；Python同C/C++一样，下标从0开始计数，结果为 y
# 倒取
name = "abcdefg"
print(name[-1])
# 越界（抛异常 IndexError）
# name = "abcdefg"
# print(name[100])

# 取字符串子串
# name = "abcdefg"
# print(name[1:3])
'''

"""
# 字符串拼接
a = 'hello'
b = 'world'
print(a + b)
print(a * 3)
print('=' * 20)
"""

'''
# 格式化字符串
num = 10
# s = 'num = %d' % num
s = 'num = {}' .format(num)
# s = f'num = {num}'   # 最推荐的高级写法，在Python3.6以后才可以使用
print(s)
'''

'''
# 获取字符串长度:应用内建函数len(Python的字符串长度与\0无关联，是C语言特有的)
# Python只有字符串类型，没有字符类型
name = 'cong'
print(len(name))
print(type(name[0]))    # 长度为1的字符串
# 少即是多：有些东西如果能由多种形式来实现，Python只保留一种形式 => [字符串(无字符)、浮点数（只有float，表示双精度，没有单精度）]
'''
'''
# 布尔类型：Python中用True和False来表示布尔值(注意：第一个字符大)
value = True
print(type(value))  # bool 类型
print(value + 1)    # 不建议使用，侧面可以得出Python中的True为1，False为0
'''
'''
# 输入输出
s = input("请输入一段内容：")
print("s:", s)

num = input('请输入一个整数：')    # input 返回值类型为字符串
print("num+1 = ", num + 1)       # 会抛异常(TypeError)
print("num+1 = ", int(num) + 1)  # 和整数相加运算时，要先把字符串转成int类型（强制类型转换）
'''
"""
a = 1
b = 2
print(a / b)
print(a // b)

# ** 表示乘方运算(记得Python的数据无上限)
a = 100
b = 20
print(a ** b)

a = 1
b = 2
c = 3
print(a < b < c)    # 与数学含义统一
print(a < c < b)
# and 表示逻辑与；or 表示逻辑或； not 表示逻辑非； 同样遵守短路求值
print(a < c and b < c)
"""
a = 'hehe'
b = 'haha'
c = 'hehe'
# print(a == b)
print(a != b)
# print(a == c)
# print(a < b)
