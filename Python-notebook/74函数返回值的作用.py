'''
思考：
    去超市购物，例如买烟，给钱之后，售货员会给我们烟这个商品。
    在函数中，如果需要返回结果给用户，则需要用到函数的返回值
'''


def buy():
    return '烟'
    print('ok')  # ok 并没有被执行


goods = buy()
print(goods)  # 输出 '烟'

'''
return 总结：
    1.负责函数返回值
    2.退出当前函数，return 下方的所有代码（函数体内部）都不执行
'''


# 案例 -- 需求：制作一个计算器，计算任意两个数字之和，并保存结果
def sum_num(a, b):
    return a + b


result1 = sum_num(10, 20)
print(result1)
