# 练习1：在屏幕上显示跑马灯文字。
# import os
# import time
# def main():
#     words='这是什么鬼东西'
#     while True:
#         os.system('cls')
#         print(words)
#         time.sleep(0.2)
#         words=words[1:]+words[0]
#words[1:]意思是去掉第一个元素（下标为0），去后面的元素进行操作
# if __name__ == "__main__":
#     main()



#默写
# import os
# import time
# def main():
#     words='qwertyuio'
#     while True:
#         os.system('cls')
#         print(words)
#         time.sleep(1)
#         words=words[1:]+words[0]
# if __name__ == "__main__":
#     main()



# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

# import random
# def random_code(code_len=4):
#     """
#     :param code_len:验证码的长度(默认4个字符)
#     :return:由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars='0123456789abcdefghijklmnopqrstuvwxyz'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
# #index是随机的一个数标
#         code += all_chars[index]
# #把对应数标的元素挨个加起来，一共加code_len次，得到的就是预期的随机验证码
#     return code

#默写
# import random
# def random_code(code_len=6):
#     element='0123456789abcdefghijklmnopqrstuvwxyz'
#     code=''
#     postion=len(element)-1
#     for _ in range(code_len):
#         index = random.randint(0,postion)
#         code += element[index]
#     return code
# print(random_code())

#默写*2
# import random
# def random_code(code_len=8):
#     element='0123456789qwertyuiopasdfghjklzxcvbnm'
#     code=''
#     postion=len(element)-1
#     for _ in range(code_len):
#         index = random.randint(0,postion)
#         code += element[index]
#     return code
# print(random_code())


# 练习3：设计一个函数返回给定文件名的后缀名。
    # """
    # 获取文件名的后缀名

    # :param filename: 文件名
    # :param has_dot: 返回的后缀名是否需要带点
    # :return: 文件的后缀名
    # """
# def get_suffix(filename, has_dot=False):
#     pos = filename.rfind('.')
# #找.所在元素的下标
#     if 0 < pos < len(filename) - 1:
# #如果.在文件名中间
#         index = pos if has_dot else pos + 1
# #如果has_dot=false,index=pos;如果has_dot=true,index=pos+1
#         return filename[index:]
#     else:
#         return ''
# filename =input('999.8.xls')
# print(get_suffix(filename))



# def get_suffix(filename,has_dot=False):
#     pos=filename.rfind('.')
#     if 0<pos<len(filename)-1:
#         index=pos if has_dot else pos+1
#         return filename[index:]
#     else :
#         return ''
# filename='888.dox'
# print(get_suffix(filename))

#默写*2
# def get_suffix(filename,has_dot=False):
#     dot_index=filename.rfind('.')
#     if 0<dot_index<len(filename)-1:
#         index=dot_index if has_dot else dot_index+1
#         return filename[index:]
#     else:
#         return ''
# filename = input('请输入文件名：')
# print(get_suffix(filename))


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     #保证m1>m2，即m1是最大数,m2是第二大
#     for index in range(2, len(x)):
#         #找下标在2~len(x)之间的元素
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
# x=[2,4,3,1]
# print(max2(x))

#练习
# def max1_2(x):
#     m1,m2=(x[0],x[1]) if x[0]>x[1] else (x[1],x[0])
#     for index in range (2,len(x)):
#         if x[index]>m1:
#             m2=m1
#             m1=x[index]
#         elif x[index]>m2:
#             m2=x[index]
#     return m1,m2
# x=[3,4,5,7,22,3]
# print(max1_2(x))

##练习*2，原来这就是冒泡排序啊

# def maxnum2(x):
#     m1,m2=(x[0],x[1]) if x[0]>x[1] else(x[1],x[0])
#     for index in range (2,len(x)):
#         if x[index]>m1:
#             m1=m2
#             m1=x[index]
#         elif x[index]>m2:
#             m2=x[index]
#     return m1,m2
# x=[99,2,3,8,10]
# print(maxnum2(x))





# 练习5：计算指定的年月日是这一年的第几天
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()

# 练习6：打印杨辉三角。



# 案例1：双色球选号。



# 综合案例2：约瑟夫环问题


# 综合案例3：井字棋游戏。