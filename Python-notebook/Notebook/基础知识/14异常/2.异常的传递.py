'''
8.异常的传递
    1.拓展命令提示符运行 py 文件 -- cmd 运行

    2.所谓异常传递，是指异常是可以嵌套书写的
'''
'''
需求：
    1.尝试以只读的方式打开 test2.txt，如果文件存在则读取文件内容，文件不存在提示用户即可
    2.读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外中止程序，则 except 捕获异常并提示用户
'''
import time

try:
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(3)
            print(content)
    except Exception:
        print('program has been accidentally killed')

except Exception:
    print('not existed')



