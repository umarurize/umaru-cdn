'''
定义别名

语法：
    1.import 模块名 as 别名 -- 模块定义别名

    2.from 模块名 import 功能 as 别名 -- 功能定义别名
'''

# 1.模块别名
import time as tt

tt.sleep(2)
print('hello')

# 2.功能别名
from time import sleep as sl
sl(2)
print('hello Python')

