# # 身份验证

# username=input("username:")
# password=input("password:")

# if username== "admin" and password=="12345":
#     print("pass")
# else:
#     print("failed")

# 分段函数求值

# x=float(input("请输入x的值："))

# # if x>1:
# #     print(3*x-5)
# # elif -1<=x<=1:
# #     print(x+2)
# # else:
# #     print(5*x+3)
# if x>1:
#     y=3*x-5
# elif -1<=x<=1:
#     y=x=2
# else:
#     y=5*x+3
# print('f(%.2f) = %.2f' % (x, y))

# # print(y)

# 英制单位与公制单位厘米互换
# x=float(input("请输入长度："))
# a=input("请输入单位（英尺/厘米）：")

# if a=="英尺" or a=="in":
#     print(x*2.54)
    
# elif a=="厘米" or a=="cm":
#     print(x/2.54)
   
# else:
#     print("请输入正确的单位")

# 百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

grade=float(input("请输入成绩："))

if grade>=90:
    print("A")
elif 80<=grade<90:
    print("B")
elif 70<=grade<80:
    print("C")
elif 60<=grade<70:
    print("D")
else:
    print("E")
  