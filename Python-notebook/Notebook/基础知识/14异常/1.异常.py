'''
异常

学习路线：
    1.了解异常
    2.捕获异常
    3.异常的else
    4.异常finally
    5.异常的传递
    6.自定义异常
'''


'''
1.了解异常
    当检测到一个错误时，解释器就无法执行了，随之会出现一些错误提示，这就是所谓的'异常'
    
异常的语法
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
'''
# 需求：尝试以 r 模式打开文件，如果文件不存在，则以 w 方式打开
try:
    f = open('test.text', 'r')
except:
    f = open('test.text', 'w')


'''
2.捕获指定异常
    2.1 什么是异常类型 
        报错信息的最后一行，冒号前提示的是异常类型
    
    2.2 捕获指定异常语法：
        try:
            可能发生错误的代码
        except 异常类型:
            如果捕获到该异常类型执行的代码
   
    2.3 注意事项：
        - 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
        - 一般 try 下面只放一行尝试执行的代码  
'''
# 异常类型
# 1.print(num) -- 异常类型 NameError
# 2.print(1/0) -- 做除法，除数不能为0 -- 异常类型 ZeroDivisionError
# 因此，书写代码的错位类型不一样，异常类型也是不一样的
try:
    print(num)
except NameError:
    print('Error') # return Error


'''
3.捕获多个指定异常
    当捕获多个异常时，可以把要捕获的异常类型名字，放到 except 后，并用元组的方式进行书写
'''
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('Error')


'''
4.捕获异常描述信息
'''
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result) # return name 'num' is not defined


'''
5.捕获所有异常
    Exception 是所有程序异常的父类
'''
try:
    print(num)
except Exception as result:
    print(result) # return return name 'num' is not defined


'''
6.异常中的else
    else 表示的是如果没有异常是要执行的代码
'''
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('Correct') # return Correct


'''
7.异常的finally
    finally 表示的是无论是否异常都要执行的代码，例如常用的关闭文件
'''
try:
    f = open('test1.txt', 'r')
except Exception as result:
    f = open('test1.txt', 'w')
    print('Error, program has created target file')
else:
    print('Correct')
finally:
    f.close()


