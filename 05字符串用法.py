# name = '张三'
# age = '18'
# nickname = '法外狂徒'
# print('姓名：' + name + ',年龄:' + str(age) + '，外号： ' + nickname)
# # 数字与字符不能直接相加 得加str（）
# # 字符串
# name2 = '李四'
# age2 = '19'
# nickname2 = '杀人帮凶'
# print('姓名：' + name2 + ',年龄:' + str(age2) + '，外号： ' + nickname2)
#
# print('----------format--------')
# # format用{}拼接
# print("姓名: {}, 年龄: {}, 外号:{}".format(name, age, nickname))
# print("姓名: {}, 年龄: {}, 外号:{}".format(name2, age2, nickname2))
#
# name_str = "姓名: {}, 年龄: {}, 外号:{}"
# print(name_str.format(name, age, nickname))
# print(name_str.format(name2, age2, nickname2))
#
# print('------%s------')
# print("姓名 : %s,年龄： %s, 外号：%s" % (name, age, nickname))
# print("姓名 : %s,年龄： %s, 外号：%s" % (name2, age2, nickname2))
#
# print('-----f-----')
# print(f"姓名: {name}, 年龄: {age}, 外号:{nickname}")
# print(f"姓名: {name2}, 年龄: {age2}, 外号:{nickname2}")
#
# # 去除符号，默认去掉空格，.strip（）
s = 'hello world !'
# print(s.strip('!'))
# print('------')
# print(s.strip().strip('!'))
# print(s)

s = s.strip()
print(s)
print(s.replace('world', 'python'))
print(s.replace('l', 'o'))
print(s.replace(' ', ''))
