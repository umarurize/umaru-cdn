'''
综合应用 -- 学员管理系统

需求：进入系统显示系统功能界面，功能如下：
    1.添加学员
    2.删除学员
    3.修改学员信息
    4.查询学员信息
    5.显示所有学员信息
    6.退出系统
系统共6个功能，用户根据说自己的需求选取
'''

'''
步骤分析：
    1.显示功能界面
    2.用户输入功能序号
    3.更具用户输入的功能序号，执行不同的功能（即调用函数）
        3.1 定义函数
        3.2 调用函数
'''


# 1.定义功能界面函数
def info_print():
    print('请选择功能------------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 20)


# 5.等待存储所有学员信息的全局变量
info = []


# 6.功能 -- 添加学员信息
def add_info():
    """添加学员函数"""
    # 用户输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 声明 info 是全局变量
    global info

    # 判断输入学员信息是否已存在，存在则不允许添加（退出函数）
    for i in info:
        if new_name == i['name']:
            print('该用户已存在，不允许重复添加')
            return

    # 如果学员不存在，执行以下添加学员信息函数
    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict) # 追加新字典到全局列表中

    print(info)


# 7.功能 -- 删除学员信息
def del_info():
    """删除学员函数"""
    # 用户输入想要删除的学员姓名
    del_name = input('请输入要删除的学员姓名：')

    global info

    # 判断输入的学员是否存在
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            print('删除成功！')
            break # 跳出遍历
        else:
            print('该学员不存在！')

    print(info)


# 8.功能 -- 修改学员信息
def modify_info():
    """修改学员信息函数"""
    # 用户输入想要修改的学员名字
    modify_name = input('请输入想要修改的学员姓名：')

    global info

    # 判断学员是否存在
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            print('修改成功！')
            break # 跳出遍历
        else:
            print('该学员不存在！')

    print(info)


# 9.功能 -- 查询学员信息
def search_info():
    """查询学员信息函数"""
    # 用户输入想要查询的学员姓名
    search_name = input('请输入想要查询的学员姓名：')

    global info

    # 判断学员是否存在
    for i in info:
        if search_name == i['name']:
            print(f"查询成功，学员的学号是{i['id']}，姓名是{i['name']}，电话号码是{i['tel']}")
            break
        else:
            print('该学员不存在！')


# 10.功能 -- 显示所有学员信息
def print_all():
    """查询所有学员信息函数"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 注：因为系统功能需要重复使用，只有用户输入6，才退出系统
while True:

    # 2.显示功能界面（调用函数）
    info_print()

    # 3.用户输入功能序号
    choose_num = int(input('请输入功能序号：'))

    # 4.按照输入的功能序号，执行不同的功能（函数）
    if choose_num == 1:
        add_info()
    elif choose_num == 2:
        del_info()
    elif choose_num == 3:
        modify_info()
    elif choose_num == 4:
        search_info()
    elif choose_num == 5:
        print_all()
    elif choose_num == 6:
       exit_flag = input('确定要退出吗？输入 yes or no：')
       if exit_flag == 'yes':
           print('系统关闭')
           break
    else:
        print('输入的功能序号有误！')

# 5.因为所有功能函数都是在操作学员信息，所有存储的学员信息必须是一个全局变量，数据类型为列表
# 每个学员的信息都是 key:value

'''
6.功能 -- 添加学员：
    1.接收用户输入学员信息，并保存
    2.判断是否已经添加该学员信息
        2.1 如果学员姓名已经存在，则报错提示
        2.2 如果学员姓名不存在，则准备空字典，将用户输入的数据追加到字典中，再将该字典追加到列表中
'''

'''
7.功能 -- 删除学员：
    1.用户输入目标学员姓名
    2.检查这个学员是否存在
        2.1 如果存在，列表删除这个字典数据
        2.2 如果不存在，则提示该用户不存在
'''

'''
8.功能 -- 修改学员信息：
    1.用户输入目标学员的姓名
    2.检查这个学员是否存在
        2.1 如果存在，则修改这位学员的信息，例如手机号
        2.2 如果不存在，则报错提示
'''

'''
9.功能 -- 查询学员信息：
    1.用户输入目标学员姓名
    2.检查这个学员是否存在
        2.1 如果存在，则显示这个学员的信息
        2.2 如果不存在，则报错提示
'''

'''
10.功能 -- 查询所有学员信息
'''