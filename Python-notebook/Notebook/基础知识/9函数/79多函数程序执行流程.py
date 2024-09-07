'''
在实际开发过程中，一个程序往往由多个函数组成，并且多个函数共享某些数据
'''

# 1.共用全局变量
glo_num = 0 # 定义全局变量


def test1():
    global glo_num # 声明全局变量
    # 修改全局变量
    glo_num = 100
    
    
def test2():
    # 调用 test1 函数中修改后的全局变量
    print(glo_num)


print(glo_num) # 返回 0，因为函数未调用
test2() # 返回 0，因为修改函数未调用
test1() # 修改全局变量
test2() # 返回 100
print(glo_num) # 返回 100，因为修改函数已调用
