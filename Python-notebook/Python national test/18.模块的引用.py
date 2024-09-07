'''
模块的引用
    1.语法 -- import
        import <模块名> as <别名>
    2.语法 -- from ... import ...
        from <模块名> import <对象、函数...>
'''


'''
两个标准库和一个第三方库
    1.标准库：
        - turtle 库
        - random 库
    2.第三方库：
        - jieba 库
'''


'''
1. turtle 库
    1.1 窗体函数：turtle.setup(width, height, startx, starty) 
      width：窗口宽度；height：窗口高度；startx：窗口与屏幕左侧距离（单位像素）；starty：窗口与屏幕顶部距离（单位像素）  
      
    1.2 画笔运动函数
        函数名                     描述
        forward(distance)         沿着当前方向（默认朝右）前进指定距离 -- 简写 fd()
        backward(distance)        沿着当前相反方向（默认朝左）后退指定距离 -- 简写 bk()
        right(angle)              向右旋转 angle 角度（角度正负数均可）   
        left(angle)               向左旋转 angle 角度（角度正负数均可）
        
    1.3 画笔状态函数
        函数名                     描述
        pensize(width)            设置画笔线条粗细，默认为 1 个像素  
        pencolor()                设置画笔线条的颜色，参数可填颜色的单词，或者 pencolor((r, g, b)) -- r, g, b 的值在 0~1之间 
        color()                   设置画笔和填充颜色（这一步不会真正填充图形，需要和 begin_fill() 和 end_fill() 配合使用）
        begin_fill()              填充图形前，调用该方法
        end_fill()                填充图形后，调用该方法
        filling()                 返回填充的状态，True 为填充，False 为未填充
        clear()                   清空当前窗口，但不改变当前画笔的属性
        reset()                   清空当前窗口所有内容  
        screensize()              设置画布窗口的宽度、高度和背景颜色
        hideturtle()              隐藏画笔  
        showturtle()              显示画笔
        isvisible()               如果 turtle 可见，则返回 True
        write(str, font = None)   输出 font 字体的字符串             
'''
import turtle as t

# 1.1 窗体函数
t.setup(600, 600, 10, 20)

# 1.2.1 fd() and bk()
# t.fd(100) -- 默认朝右
# t.bk(100) -- 默认朝左

# 1.3.1 pensize(width)
t.pensize(2) # 这里就将线条的宽度设置为了 2 个像素

# 1.3.2 pencolor()
# t.pencolor('red') -- 这里就将线条的颜色设置为了红色

# 1.3.3 color()
t.color('red', 'blue')

# 1.3.4-1 begin_fill()
t.begin_fill()

# 1.2.2 right() and left()
for i in range(1, 5, 1): # 或者 for i in range(4):
    t.fd(100)
    t.left(90)

# 1.3.5 filling()
print(t.filling()) # return True，表明已填充

# 1.3.4-2 begin_end()
t.end_fill()

# 1.3.6 clear()
# t.clear()

# 1.3.7 reset()
# t.reset()

# 1.3.9 hideturtle() and showturtle() and isvisible()
t.hideturtle()

# 1.3.10 write(str, font = None)
t.write('这是一个正方形')

t.done()