# 11/15###################################################################################
# if/else/elif���
'''
if a>b:
    do_soming()


if expression:
        do_something1   # ÿ��4���ո�(���ܶ�/��)
        do_something2
next_something      # һ�����ӡ

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
    if result == '1':       # ��������ֹ��Ƕ��
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

# ѭ��ִ������print
counter = 0
while counter < 3:
    print 'loop %d' % counter
    counter += 1
'''
"""
# Python��1��ӡ��10
# ��1
num = 1
while num <= 10:
    print(num)
    num += 1

# ��2
for num in range(1,11):
    print(num)
"""
"""
a = [3,7,1,9]    # �����ַ����е�ÿһ��Ԫ��
a = 'holdon'     # �����ַ����е�ÿһ���ַ�
for num in a:    # ��ȡa�е�����
    print(num)

a = {'ip':'127.0.0.1','port':'80'}
for key in a:
    print(key,a[key])

# �ڽ�����range��range�Ĳ�����������ǰ������ʾ����ҿ�����������ʾ����
# forѭ��ִ��10�δ�ӡ����1��ʼ����10������[1,11)��
for num in range(1,11):
    print(num)

# ����[0, 100)�����е�ż��
for i in range(0, 100, 2):
    print i

# break��continue
for num in range(1,10):
    if num % 3 == 0:
# break
        continue
    print(num)

for i in range(1,30):
    if i % 3 != 0:
        continue
    print(i)

# pass(�����)
if a == 10:
    pass
else:
    print('hello')
"""

# ��ͳд��
'''
a = [1,2,3,4,5]
b = []
for num in a:
    b.append(num ** 2)      # **��ʾ�˷�
    print(b)

# �б��Ƶ���������
a = [1,2,3,4,5]
# b = [x ** 2 for x in a]
b = [x ** 2 for x in a if x % 2 == 1]   # ����
print(b)


# ���� [0, 4) �����ֵ�ƽ������
squared = [x ** 2 for x in range(4)]
print(squared)


# ��ȡ [0, 8) �����е����е�����
evens = [x for x in range(0, 8) if x % 2 == 1]
print evens
'''