'''
综合应用 -- 烤地瓜

需求：
    1.被烤的时间和对应的地瓜状态
        0-3 分钟：生的
        3-5分钟：半生不熟
        5-8分钟：熟的
        超过8分钟：烤糊了

    2.添加的调料：
        用户可以按自己的意愿添加调料

步骤分析：
需求中涉及一个事物：地瓜，因此需要定义一个类：地瓜类
    1.定义地瓜类：
        1.1 地瓜的属性：
            - 被烤的时间
            - 地瓜的状态
            - 添加的调料
        1.2 地瓜的方法
            - 被烤
                > 用户根据意愿设定每次烤地瓜的时间
                > 判断地瓜被烤的总时间是在哪个区间，修改地瓜状态
            - 添加调料
                > 用户根据意愿设定添加调料
                > 将用户添加的调料存储
        1.3 显示对象信息
'''


class SweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟的'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}，添加的调料有{self.condiments}'


digua1 = SweetPotato()
print(digua1)

digua1.cook(6)
digua1.add_condiments('酱油')
print(digua1)

