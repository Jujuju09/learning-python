# 计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

# import random

# anser = random.randint(1,100)
# count=0
# while True:
#     num = int(input("num="))
#     count +=1
#     if num>anser :
#         print("小一点")
#     elif num<anser:
#         print("大一点")
#     else:
#         print("bingo!")
#         break
# print("总共猜了%d次"%(count))


# 输出乘法口诀表(九九表)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j), end='\t')
#     print()
