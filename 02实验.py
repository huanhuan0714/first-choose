num = 371
g = num % 10  # 371/10=37.1 取余数1
s = int(num / 10 % 10)  # 371/10=37.1取整数7
b = int(num / 100 % 10)
print(g, s, b)
num_result =g ** 3 + s ** 3 + b ** 3
print(num_result)