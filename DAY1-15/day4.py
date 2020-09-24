# 寻找水仙花数。

# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

#一个三位数，寻找他的每个位的数字。

# for num in range(99,1000):
#     a = num%10
#     b = num//10%10
#     c = num//100
#     if num==a**3+b**3+c**3:
#         print(num)
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)


#把输入的数字翻转

# num=int(input("请输入要翻转的数字："))
# re=0
# while num>0:
#     re=re*10+num%10
#     num=num//10
# print(re)

# 百钱百鸡问题。

# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

# for x in range(0,20):
#     for y in range(0,33):
#         z=100-x-y
#         if 5*x+3*y+z/3==100:
#             print(x,y,z)

# CRAPS赌博游戏。

# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜
# ；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。

# from random import randint

# money=1000
# print("你的本金为：%d"%(money))
# while money>0: 
#     debt=int(input("请输入赌注金额："))
#     go_on=False
#     if 0<debt<=money:
#         frist= randint(1,6)+randint(1,6)
#         print("您摇出了：",frist)
#         if frist==7 or frist==11:
#             money=money+debt
#             print("玩家胜,您的资金为%d"%(money))
#         elif frist==2 or frist==3 or frist==12:
#             money=money-debt
#             print("庄家胜,扣除资金%d，您的资金为%d"%(debt,money))
#         else:
#             go_on=True
#         while go_on:
#             go_on=False
#             point=randint(1,6)+randint(1,6)
#             print("您摇出了：",point)
#             if point==7:
#                 money=money-debt
#                 print("庄家胜,扣除资金%d，您的资金为%d"%(debt,money))
#             elif point==frist:
#                 money=money+debt
#                 print("玩家胜,您的本金为%d"%(money))
#             else:
#                 go_on=True
#     else:
#         print("你没有那么多资金，你现在的资金为",money)
# print("你破产了，游戏结束！")


# 生成斐波那契数列的前20个数。

# 说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在
# 《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
# 所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，
# 从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
# 斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
# fe=0
# fe1=1
# i=0
# while i<20:
#     fe=fe+fe1
#     fe1=fe-fe1
#     i=i+1
#     print(fe)
# 找出10000以内的完美数。

# 说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

l=[]
for i in range(1,1000):
    k=0
    for j in range(1,i):
        if i%j==0:
            k +=j
    if k==i:
        l.append(i)
print(l)


# 输出100以内所有的素数。

# # 说明：素数指的是只能被1和自身整除的正整数（不包括1）。
# l=[]
# for x in range(100):
#     if x<2:
#         continue
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         l.append(x)
# print(l)