'''
综合应用 -- 搬家具

需求：将小于房子剩余面积的家具搬到房子中

步骤分析：
需求中涉及两个事物：房子和家具。因此案例涉及两个类：房子类和家具类
    1.定义类：
        1.1 房子类：
            - 实例属性
                > 房子地理位置
                > 房子占地面积
                > 房子剩余面积
                > 房子内家具列表
            - 实例方法
                > 容纳家具
            - 显示房屋信息
        1.2 家具类：
            - 家具名称
            - 家具占地面积
'''


class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def add_furniture(self, item):
        """搬家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法搬入')

    def __str__(self):
        return f'房子的地理位置在{self.address}，房屋面积是{self.area}，剩余面积是{self.free_area}，家具有{self.furniture}'


bed = Furniture('床', 6)
sofa = Furniture('沙发', 10)

home1 = Home('北京', 100)
home1.add_furniture(bed)
home1.add_furniture(sofa)
print(home1)