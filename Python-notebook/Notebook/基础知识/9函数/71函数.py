'''
函数 -- 非常重要，应用场景很广泛
学习函数的路线：
    1.函数的作用
    2.函数的使用步骤
    3.函数的参数作用
    4.函数的返回值作用
    5.函数的说明文档
    6.函数嵌套
'''

'''
1.函数的使用步骤：
    1.1 定义函数
    1.2 调用函数
    
语法：
    def 函数名(参数):
        代码1
        代码2
    
    调用函数 -- 函数名(参数)

注意:
    1.不同的需求下，参数可有可无
    2.函数必须先定义再调用
'''

# 案例1：复现 ATM 取钱框架
'''
1.搭建整体框架
    print('密码正确登录成功')
    
    # 显示'选择功能'界面
    
    print(''查询余额完毕)
    
    # 显示'选择功能'界面
    
    print('取了2000元钱')
    
    # 显示'选择功能'界面
    
2.确定'选择功能'界面内容
    print('查询余额')
    print('存款')
    print('取款')
    
3.封装功能

4.调用函数
'''

# 1.确定整体功能并封装函数
def sel_func():
    print('查询余额')
    print('存款')
    print('取款')

# 2.搭建整体框架并用函数
print('登录成功')
sel_func()
print('您的余额是1000元')
sel_func()
print('取了100元')
sel_func()

