help(len) # 返回了 len 的解释说明 -- 因此函数 help() 起到了说明文档的作用

'''
函数的说明文档：
语法格式：
    def 函数名(参数):
        """ 说明文档 """
        执行代码
        .....

查看说明文档语法：
    help(函数名)
'''


def sum_num(a, b):
    """求和函数"""
    return a + b


help(sum_num) # 返回 '求和函数'


def sum_num1(a, b):
    """
    求和函数 sum_num 说明文档
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


help(sum_num1) # 返回多行说明文档



