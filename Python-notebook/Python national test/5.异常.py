'''
异常处理（try-except）

语法：
    try:
        尝试执行代码1
    except:
        发生错误时执行的代码2
'''
# 1.
try:
    score = float(input('请输入您的分数：'))
except:
    print('您输入的数据类型无效...')


# 2.捕获指定异常
try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('除数不能为 0') # 捕获指定异常，输出这句话
except:
    print('Error') # pass