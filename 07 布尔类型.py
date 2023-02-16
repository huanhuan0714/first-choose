# 真 对 满足条件
true = True
# 假 错 不满足条件
flase = False
# true 1
# flase 0
"""
布尔类型转换
数字类型：除了0都是true
字符串：除了空字符串之外都是true
对象/变量：除了空对象之外true
"""
# 判断条件返回的都是布尔类型
print(4 > 5)
print(4 < 5)
print('----------')
# 转化数字
print(bool(0))
print(bool(1))
print(bool(3))
print(bool(-1))
# 转化字符串
print('---------')
print(bool(''))
print(bool(' '))
print(bool('sdiashid '))

# 转化对象
print('--------')
print(bool(None))
print(bool(float))
print(bool(int))



r = 4 > 5
if 4 > 5:
    print('4大于5')
else:
    print('4小于6')

num = 0
if num:
    print('spideman')
else:
    print('ironman')