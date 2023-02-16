"""逻辑运算符"""
# and 条件1 and 条件2 都满足则返回true 否则返回False
# or 条件1 or 条件2 满足条件1或者条件2 返回true 都不满足则返回false
# not 如果是true就变false 如果是false就变true
two = 2
four = 4
print(two > four)

true = True
false = False

print(True and True)
print(True and False)
print(False and False)
print((4 > 3) and (-5 < -2))
print('-----------')

print(True or True)
print(True or False)
print(False or False)
print('-----------')
print(not true)
print(not false)