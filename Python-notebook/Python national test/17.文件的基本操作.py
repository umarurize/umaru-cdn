'''
文件的基本操作
    1. 文件的类型
        - 文本文件：一般由单一特定编码的字符组成，如 Unicode 编码，内容容易统一展示和阅读。
        由于文本文件存在编码，可以看作是存储在磁盘上的长字符串，如一个 txt 格式的文本文件
        - 二进制文件：直接由 0 和 1 组成，没有统一的字符编码，文件内部数据的组织格式与文件用途有关。
        如 png 格式的图片文件、mkv 格式的视频文件

    2. 文件的操作
        - 打开文件 .open() 分读写模式
        - 关闭文件 .close()
'''


'''
1.文件操作-打开文件
    打开模式            描述
    r                  只读模式；如果文件不存在，则报错
    w                  覆盖写模式，文件不存在则创建，存在则完全覆盖原文件
    x                  创建写模式，文件不存在则创建，存在则报错
    a                  追加写模式，文件不存在则创建，存在则在原文件末尾追加内容
    b                  二进制文件模式
    t                  文件文本模式，默认值
    +                  与 r、w、x、a 组合使用，在原功能基础上增加同时读写功能       
'''


'''
1.1 文件操作-读
    方法                描述
    f.read(size)        从文件中读入整个文件内容，参数可选，如果有参数，读入 size 长度的字符串或字节流
    f.readline(size)    从文件中读取一行内容，参数可选，如果有参数，读入该行前 size 长度的字符串或字节流
    f.readlines(hint)   从文件中读取所有行，以每行为元素返回一个列表，参数可选，如果有参数，读入 hint 行
    f.seek(offset)      改变当前文件操作的指针位置；offset的值：0-为文件开头、1-从当前位置开始、2-为文件末尾    
'''
f = open('test.txt', 'r', encoding = 'utf-8') # 这是一种相对路径的写法

# 1.1.1 f.read(size)
# con = f.read()
# print(con) --  return 整个文件的内容

# 1.1.2 f.readline(size)
# con = f.readline()
# print(con) return 大家好，欢迎学习\n -- 即文件中第一行内容，注意后面会跟一个换行符
# con = f.readline(4)
# print(con) return 大家好， -- 即文件第一行前 4 个字符的内容

# 1.1.3 f.readlines(hint)
# con = f.readlines()
# print(con) return ['大家好，欢迎学习\n', '国家计算机 Python 二级'] -- 即返回一个列表，列表中的每一个元素是每一行，注意会跟一个换行符
# con = f.readlines(1)
# print(con) return ['大家好，欢迎学习\n'] -- 即只读一行，并返回一个列表

# 1.1.4 f.seek(offset)
# 注意进行文件指针操作时，需要以二进制模式操作

f.close()


'''
1.3 文件操作-写
    方法                      描述
    f.write(s)                向文件写入一个字符串或字节流
    f.writelines(lines)       将一个元素为字符串的列表整体写入文件  
'''
f = open('test1.txt', 'w', encoding = 'utf-8')

# 1.3.1 f.write(s)
f.write('hello world\n')
f.write('your name\n')

# 1.3.2 f.writelines(lines)
lines = ['你好世界\n', '你的名字\n']
f.writelines(lines)
f.close()

# 追加内容
fo = open('test1.txt', 'a', encoding = 'utf-8')
fo.write('nb')
fo.close()


