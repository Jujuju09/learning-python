# 用for循环实现1~100求和
# sum=0
# x=0
# for x in range(0,101):
#     sum +=x
# print(sum)

# 用for循环实现1~100之间的偶数求和

# sum=0
# for x in range(2,101,2):
#     sum += x
# print(sum)

# sum=0
# for x in range(1,101):
#     if x%2==0:
#         sum +=x
# print(sum)

# 输入非负整数n计算n!
# mul=1
# n=int(input("num="))
# for x in range(1,n+1):
#     mul *=x
# print(mul)

# 输入一个正整数判断它是不是素数
# y=True
# n=int(input("n="))
# for i in range(2,n):
#     if n%i==0:
#         y= False
#         break
# else:
#     y=True
# print(y)

# from math import sqrt
# num=int(input("num="))
# mid=int(sqrt(num))
# is_prime=True
# #mid用来减少循环次数
# for x in(2,mid+1):
#     if num%x==0:
#         is_prime=False
#         break
# if is_prime==True and num !=1:
#      print("是素数")
# else:
#     print("不是素数")


# for a in range(1,10):
#     print (a)

 


# 输入两个正整数计算最大公约数和最小公倍数

# num1=int(input("num1="))

# num2=int(input("num2="))
# if num1>num2:
#     (num1,num2)=(num2,num1)

# for a in range(num1,0,-1):
#     if num1%a==0 and num2%a==0:
#         print(a)
#         print(num1*num2//a)
#         break

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

# 打印各种三角形图案
# *
# **
# ***
# ****
# *****
#     *
#    **
#   ***
#  ****
# *****
#     *
#    ***
#   *****
#  *******
# *********



# row =int(input("请输入行数："))
# for i in range(row):
#     for i in range(i+1):
#         print("*",end="")
#     print()


row=int(input("请输入行数："))
# for i in range(row):
#     for i in range(i+1):
#         print(" ","*",end="")
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()


# for i in range(row):
#     for _ in range(row-i-1):
#         print(" ",end="")
#     for _ in range(i*2+1):
#         print("*",end="")
#     print()

for i in range(row):
    for _ in range(row-i-1):
        print(" ",end="")
    for _ in range(2*i+1):
        print("*",end="")
    print()

# fe=0
# fe1=1
# for i in range(0,row):
#     fe += fe1
#     fe1=fe-fe1
#     print(fe)


    

# 用while循环实现1~100求和
# sum=0
# num=0
# while num<=100:
#     sum +=num
#     num +=1
# print(sum)
    

# 用while循环实现1~100之间的偶数求和

# sum=0
# num=1
# while num<=100:
#     sum +=num
#     num +=2
# print(sum)

