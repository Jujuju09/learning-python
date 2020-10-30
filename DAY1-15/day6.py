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
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


##begin
# def alg(x,y):
#     if x>y:
#         (x,y)=(y,x)
#     for i in range(x,0,-1):
#         #(x,0,-1),指的是从x到0倒着取值
#         if x%i==0 and y%i==0:
#             break
#     return i

# def lcm(x,y):
#     return x*y//alg(x,y)

# print(alg(9,88))
# print(lcm(9,88))


# 练习2：实现判断一个数是不是回文数的函数。
##回文数的定义是，正着读跟反着读是一样的结果如，121，反着也是121，所以是回文数
##自己写的
# def palin(x):
#     y=x
#     re=0
#     while x>0:
#         re=re*10+x%10
#         x=x//10
#     if y == re:
#         return True
#     else:
#         return False

# print(palin(1111))
##答案
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num





# 练习3：实现判断一个数是不是素数的函数。

# def is_prime(x):
#     for i in range(2,x-1):
#         if x%i==0:
#             return False
#         else :
#             return True
# print(is_prime(1))

##THE ANWSER
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


# 练习4：写一个程序判断输入的正整数是不是回文素数。
# if __name__ == '__main__':
#     num=int(input("请输入正整数:"))
#     if is_prime(num) and is_palindrome(num):
#         print("%d是回文素数"%num)
#     else:
#         print("%d不是回文素数"%num)


# def foo():
#     b = 'hello'

#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)

#     bar()
#     # print(c)  # NameError: name 'c' is not defined

# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()




# def foo():
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)



ef foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)





