'''
模块和包

学习路线：
    1.了解模块
    2.导入模块
    3.制作模块
    4.__all__
    5.包的使用方法
'''


'''
1.了解模块
    模块就是一个 Python 文件，它提前定义好了一些功能、函数.....
'''


'''
2.导入模块
    - import 模块名
    - from 模块名 import 功能名
    - from 模块名 import*
    - import 模块名 as 别名
    - from 模块名 import 功能名 as 别名
'''
# 2.1
# 导入模块：import 模块名 -- 建议这种方法只导入一个模块
# 调用功能：模块名.功能名()
import math

print(math.sqrt(9)) # return 3.0

# 2.2
# 导入模块：from 模块名 import 功能名
# 调用功能：不需要书写 模块名.功能名
from math import sqrt
print(sqrt(16)) # return 4.0

# 2.3
# 导入模块：from 模块名 import*
# 调用功能：不需要书写 模块名.功能名
from math import*
print(sqrt(25)) # return 5.0

