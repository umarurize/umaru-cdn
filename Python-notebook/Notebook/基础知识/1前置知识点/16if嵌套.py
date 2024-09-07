'''
需求：
坐公交车，如果有钱可以上车，没钱不能上车；
上车后如果有空座，则可以坐下；如果没有就要站着
'''

money = int(input('您有多少钱：'))
seat = 0

if money >= 2:
    print('请上车')
    if seat == 1:
        print('车上有空座，请找座位坐下')
    else:
        print('不好意思没位置了，站稳扶好')
else:
    print('不准上车')

