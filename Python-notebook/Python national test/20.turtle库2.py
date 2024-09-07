'''
turtle 库2

1.画笔运动函数-补充
    函数名                 描述
    goto(x, y)            移动到绝对坐标 (x, y) 处 -- 默认画笔处于 (0, 0) 位置
    setx(x)               修改画笔的横坐标为 x，纵坐标不变
    sety(y)               修改画笔的纵坐标为 y，横坐标不变
    setheading(angle)     设置当前朝向为 angle 角度 -- 默认是 0°，即箭头朝右
    home()                画笔位置回到原点，朝向东（即朝右）

    circle(radius, e)     绘制一个指定半径 r 和角度 e 的圆或弧形 -- 默认逆时针方向绘制
    dot(size, color)
    undo()                撤销画笔的最后一步动作
    speed()               设置画笔的绘制速度，参数为 0~10 之间

2.画笔状态函数-补充
    函数名             描述
    pendown()          放下画笔
    penup()            提起画笔，与 pendown() 配对使用
'''
import turtle as t

t.setup(600, 600, 10,10)

# 1.1 circle(radius, e)
# t.circle(60) 默认是逆时针方向绘制，这里改成 -60 即顺时针方向绘制
# t.circle(60, 180) 画了一个半弧
t.circle(60, steps = 8) # 即半径 60 的圆里的内切多边形

t.penup()

# 1.2 goto(x, y)
t.goto(60, 100)

t.pendown()

# 1.3 setx(x) and sety(y)
t.setx(120)
t.sety(0)

# 1.4 setheading()
t.setheading(90)

# 1.5 home()
t.home()

# 1.6 dot(size, color)
t.dot(10, 'red')


'''
2 pendown() and penup() 
t.fd(100)
t.penup()
t.left(90)
t.fd(20)
t.left(90)
t.pendown()
t.fd(100)
t.hideturtle()
'''

t.done()
