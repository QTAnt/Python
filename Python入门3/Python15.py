# 11/15###################################################################################
# if/else/elif语句
'''
if a>b:
    do_soming()


if expression:
        do_something1   # 每级4个空格(不能多/少)
        do_something2
next_something      # 一定会打印

if expression:
        do_something1
else:
        do_something2

result = input('What to eat today? 1 Cold 0 Hot')
if result == '1':
    print('ice cream')
else:
    print('huoguo')


result = input('What to eat today? 1 Cold 0 Hot')
if result == '1':
    print('ice cream')
    print('ice cream')
    if result == '1':       # 可以无休止的嵌套
        print('rice')
        if result == '1':
            print('rice')
elif result == '0':
    print('huoguo')
    print('huoguo')
else:
    print('salad')


while expression:
    do_something

# 循环执行三次print
counter = 0
while counter < 3:
    print 'loop %d' % counter
    counter += 1
'''
"""
# Python从1打印到10
# 法1
num = 1
while num <= 10:
    print(num)
    num += 1

# 法2
for num in range(1,11):
    print(num)
"""
"""
a = [3,7,1,9]    # 遍历字符串中的每一个元素
a = 'holdon'     # 遍历字符串中的每一个字符
for num in a:    # 读取a中的内容
    print(num)

a = {'ip':'127.0.0.1','port':'80'}
for key in a:
    print(key,a[key])

# 内建函数range：range的参数有三个，前两个表示左闭右开，第三个表示步长
# for循环执行10次打印（从1开始，到10结束，[1,11)）
for num in range(1,11):
    print(num)

# 遍历[0, 100)区间中的偶数
for i in range(0, 100, 2):
    print i

# break，continue
for num in range(1,10):
    if num % 3 == 0:
# break
        continue
    print(num)

for i in range(1,30):
    if i % 3 != 0:
        continue
    print(i)

# pass(空语句)
if a == 10:
    pass
else:
    print('hello')
"""

# 传统写法
'''
a = [1,2,3,4,5]
b = []
for num in a:
    b.append(num ** 2)      # **表示乘方
    print(b)

# 列表推导（解析）
a = [1,2,3,4,5]
# b = [x ** 2 for x in a]
b = [x ** 2 for x in a if x % 2 == 1]   # 奇数
print(b)


# 生成 [0, 4) 的数字的平方序列
squared = [x ** 2 for x in range(4)]
print(squared)


# 获取 [0, 8) 区间中的所有的奇数
evens = [x for x in range(0, 8) if x % 2 == 1]
print evens
'''