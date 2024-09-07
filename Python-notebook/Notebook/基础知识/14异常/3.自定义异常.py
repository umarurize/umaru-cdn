'''
9.自定义异常
    1.作用：报错 -- 非语法报错，而是不符合程序逻辑要求的错误

    2.在 Python 中，抛出自定义异常语法为 raise 异常类对象
'''


'''
需求：
    密码长度不足，报错异常（用户输入密码，如果输入的长度不足3位，则报错，即抛出自定义异常，并捕获该异常）
    
步骤分析：
    1.自定义异常类 -- 注意：定义异常类，要继承 Exception
    2.抛出异常
    3.捕获异常
'''


class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'your password length is {self.length}, which is not allowed to be less than {self.min_len} words'


def main():
    try:
        password = input('please enter your password:')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)
    except Exception as result:
        print(result)
    else:
        print('successful!')

main()



