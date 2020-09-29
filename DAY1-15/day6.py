# 上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案。



# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)

# 用函数去计算

# def fac(num):
#     result=1
#     for i in range(1,num+1):
#         result *=i
#     return result

# m=int(input("m="))
# n=int(input("n="))

# print(fac(m)//fac(n)//fac(m-n))

# from random import randint

# def roll(n=2):
#     total=0
#     for _ in range(n):
#         total +=n
#     return total
# def add(a=0,b=0,c=0):
#     return a+b+c
# print(roll())

# print(roll(3))
# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))

# print(add(c=50, a=100, b=200))

# def add(*args):
#     total=0
#     for val in args:
#         total += val
#     return total

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))



# def foo():
#     print('hello, world!')


# def foo():
#     print('goodbye, world!')


# # 下面的代码会输出什么呢？

# foo()


# from module1 import foo

# foo()

# from module2 import foo
# foo()


# import module1 as foo1

# import module2 as foo2

# foo1.foo()
# foo2.foo()





# def foo():
#     pass


# def bar():
#     pass


# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()


# 练习1：实现计算求最大公约数和最小公倍数的函数。

# def alg(n,m):
#     for i in range(0,n*m//2+1):
#         if n%i==0 and m%i==0:

m=2
n=4
if m>n:
    (m,n)=(n,m)
for i in range(n,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        
        break
                       

# 练习2：实现判断一个数是不是回文数的函数。



# 练习3：实现判断一个数是不是素数的函数。



# 练习4：写一个程序判断输入的正整数是不是回文素数。



