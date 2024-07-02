'''
需求分析
1.参与游戏的玩家
    玩家
        手动出拳
    电脑
        随机出拳
2.判断输赢
    玩家获胜
    玩家      电脑
    石头      剪刀
    剪刀      布
    布       石头
'''

'''
拓展：随机数运算
step1-导出 random 模块：
    import 模块名
step2-使用 random 模块中的随机整数功能
    random.randint(开始,结束)
'''
# 电脑随机出拳
import random
AI = random.randint(0,2)

player = int(input('请出拳[0--石头；1--剪刀；2--布]：'))

if ((player == 0) and (AI == 1)) or ((player == 1) and (AI == 2)) or ((player == 2) and (AI == 0)):
    if (player == 0) and (AI == 1):
        print('你出的石头，电脑出的剪刀，你赢了！')
    elif (player == 1) and (AI == 2):
        print('你出的剪刀，电脑出的布，你赢了！')
    else:
        print('你出的布，电脑出的石头，你赢了！')
elif player == AI:
    if player == AI == 0:
        print('你们出的都是石头，平局..')
    elif player == AI == 1:
        print('你们出的都是剪刀，平局..')
    else:
        print('你们出的都是布，平局..')
else:
    if (player == 0) and (AI == 2):
        print('你出的石头，电脑出的布，你输了')
    elif (player == 1) and (AI == 0):
        print('你出的剪刀，电脑出的石头，你输了')
    else:
        print('你出的布，电脑出的剪刀，你输了')

