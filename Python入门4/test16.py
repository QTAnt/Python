# 11/16###################################################################################
# ***函数***
# 函数（没有返回类型）Python是一动态类型（想返回什么类型，可以在程序运行过程中决定），类型可以动态改变
# js也是动态类型，同Python
# 定义一个函数
'''
def add(x,y):        # add,函数名；x、y是形参，参数也没有类型
    # 函数体
    ret = x+y
    return ret
# Python里没有函数重载，如果出现同名函数，会出现相互覆盖的情况（后定义的覆盖之前定义的）
def add(x,y,z):
    return x+y+z
# 调用:Python使用()来调用函数
ret = add(10,11)
print(ret) 


# 默认参数
def add(x=0,y=0):
    ret = x+y
    return ret
ret = add(10)       # x为10，y为0
print(ret)


# Python的函数返回值，一次调用可以返回多个值，之间用'，'分隔开
# 虽然返回多个值，但是返回值也可以用一个值来接收，查看该值的类型后发现为'tuple'
# 因此当一个函数返回多个值的时候，返回值实际是一个元组，然后应用unpack(解包)语法把元组中的n个内容拆解到多个变量中
def get_point():
    x = 10
    y = 11
    return x, y

# x,y = get_point()
# tmp = get_point()
_,y = get_point()
print(_,y)
# print(type(tmp))

# 函数也是对象
# 对象的一属性及方法的集合，包含成员变量，方法。
# 函数也是一对象，对象之间可以相互赋值；对象可作为一个函数的参数、返回值；一个函数也可以作为另外一个函数的参数、返回值
def get_point():
    x = 10
    y = 11
    return x, y

print(type(get_point))
'''
# ***文件函数***
# shell 的文件操作更简单，应用重定向（>、<）即可完成文件的读、写操作
# 读
'''
# open(绝对/相对文件路径，打开的方式rwatb（读、写、追加、按文本方式读写、按二进制方式读写）)，返回值是一个文件对象
# 与Linux系统调用的open完全不一样，Linux返回的是一个比较底层的文件描述符
# 
f = open('F:/test.txt','r')
# f.read()        # 不常用
# f.readline()    # 读一行，不常用
# f.readlines()   # 把文件读完（干净）

# 返回值是一个列表（每个元素，就是文件的一行数据）
a = f.readlines()
print(a)
f.close()       
# 打开文件后，不用的时候一定要及时关闭，以防有其他隐患。
# 当对象f的生命周期结束了的时候，会引发gc的垃圾自动回收机制，
# 但是gc的回收很可能不够及时，不够及时就意味着有段时间文件虽然没用，但是依然是打开状态，后续再想打开其他文件的话就会失败
# 原因：文件资源泄漏（一个进程能打开的句柄数是有限的。进程里的文件描述表有上限，打开数量达到上限时，就不能再打开其他的了，此时一定会打开失败）

f = open('F:/test.txt','r')
# f是一个文件句柄, 是一个可迭代的对象. 可以直接使用for循环按行读取文件内容
for line in f:
    #print(line)   # 自身有换行
    print(line, end='')
f.close()

# 写
f = open('F:/test.txt','w')
f.write('hello world!')
f.close()
'''

# 统计文本中的词频
'''
# strip：str方法，功能是去掉字符串头和尾的空白字符（空格、制表符、换行符、垂直制表符、翻页符...）
# C++的getline:一次读一行，没有'\n';Python包含（不包含的方法：应用切片[0:-1]，但是这样会把最后一行的最后一个字符误删）
# Python中字典的[]行为与C++中的map很相似，都是“key存在，就是查找；不存在，是插入”
f = open('F:/test.txt','r')

word_dict = {}
# 按行读取,应用字典
for word in f:
    # word = word[0:-1]     
    # 上一行的注释： 应用切片[0:-1]，但是这样会把最后一行的最后一个字符误删(Python3中会有这样的问题，但是我的Python2好像不存在这样的问题，但是统计的顺序变了)
    
    word = word.strip()     # 去掉字符串头和尾的空白字符
    if word in word_dict:   # in 表示查找，word是否在字典的key中存在(不管value)；in在列表、字符串中时可以
        word_dict[word] += 1
    else:
        word_dict[word] = 1

f.close()
print(word_dict)
'''

# ***模块***
# 模块（任意一个.py文件都算是一个模块，模块名是去掉.py后缀）
# 模块也是对象
# 想在 Untitled.py中调 calc.py里的代码

# 注意：calc.py这个文件必须放在当前目录中，或者系统目录中（Python安装目录里面有一个专门可以放文件的文件夹）
# calc.py：
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def devide(x,y):
    return x/y

# Untitled.py
import calc     # 先导入模块

print(calc.add(10,11))
print(calc.sub(10,11))
print(calc.mul(10,11))
print(calc.devide(10,11))
print calc.path # 可以打印出模块查找的路径