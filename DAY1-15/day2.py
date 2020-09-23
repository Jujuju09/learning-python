# 数据类型
# 1.整型
# 2.浮点型
# 3.字符串型
# 4.布尔值
# 5.复数型：3+5j

# 基本算数
# a=987
# b=21
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# 判断字符串类型
# a=99
# b=12.123
# c=1+5j
# d='hello'
# e=False
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# %d是整数占位符，%f是浮点数占位符
# //是整除，%%是取余，**幂运算

# a=10
# b=3
# a +=b  
# # a=13
# a *= a+2 
# # a=13*15=195
# print(a)


# 华氏温度转为摄氏温度

# C=(F-32)÷1.8

# a= float(input('请输入华氏温度：'))

# b=(a-32)/1.8

# # print('%.1f华氏度 = %.1f摄氏度' % (a, b))  
# # 或者下面这种写法
# print(f'{a:.1f}华氏度 = {b:.1f}摄氏度')

# 输入圆的半径，计算圆的面积和周长

# r=float(input('请输入圆的半径'))

# c=2*3.14*r

# s=3.14*r**2

# print('周长=%.1f,面积=%.1f'%(c,s))



# 输入年份判断是不是闰年
year=int(input("请输入年份："))

c=year%4==0 and  year%100 !=0 or year%400==0

print(c)


