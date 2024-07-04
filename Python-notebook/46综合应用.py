# 需求：有8位老师，3个办公室；将8位老师随机分配到3个办公室

'''
需求分析：
    1.准备数据
        1.1 8位老师的数据 -- 用列表存储
        1.2 3个办公室数据 -- 列表嵌套
    2.分配老师到办公室
        2.1 随机分配
        即办公室列表追加老师的名字数据
    3.验证是否分配成功
        3.1 print 办公室信息（每个办公室的人数和对应老师的名字）
'''

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 8位老师的数据
offices = [[], [], []] # 3个空的办公室

# 分配老师到办公室 -- 将每个老师放到办公室列表 -- 遍历老师列表数据
import random

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

# 为办公室子列表添加编号，用于区分
i = 1

# 验证是否分配成功
for office in offices:
    print(f'办公室{i}的人数是{len(office)}, 老师分别是：')
    for name in office:
        print(name)
    i += 1

