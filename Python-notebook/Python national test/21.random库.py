'''
Python 给出的随机数其实是伪随机数，它是基于一定的算法给出的，即 seed，默认 seed 是系统时间

random 库
    函数名                         描述
    seed(a = None)                初始化随机数种子，默认值为当前系统时间
    random()                      生成一个 0.0 ~ 1.0（不含1.0）的随机小数
    randint(a, b)                 生成一个 [a, b] 之间的随机整数
    getrandbits(k)                生成一个 k 比特长度的随机整数
    randrange(start, stop, step])     生成一个 [start, stop) 之间以 step 为步长的随机整数
    uniform(a, b)                 生成一个 [a, b] 之间的随机小数
    choice(seq)                   从序列类型（列表或元组）中随机返回一个元素
    shuffle(seq)                  将序列类型中的元素随机排列，返回重新排列后的序列
    sample(pop, k)                从 pop 中随机取 k 个元素，以列表类型返回
'''
import random as r

# 1.random()
print(r.random()) # return 0.3129200641290053 -- 即随机返回 [0.0, 0.1) 之间的浮点数

# 2.seed(a = None)
# r.seed(10)
# print(r.random()) return 0.5714025946899135

# r.seed(10)
# print(r.random()) return 0.5714025946899135 -- 两次返回的随机数相同，说明只要给出随机数种子，就会基于此种子算出随机数，结果也是必然相同的

# 3.randint(a, b)
print(r.randint(1, 10)) # return [1, 10] 区间的随机整数

# 4.getrandbits(k) -- 不常用
num = r.getrandbits(4)
print(num)
num1 = bin(num)
print(num1)

# 5.randrange(start, stop, step)
print(r.randrange(1, 100, 2)) # return [1, 100) 区间，步长为2 的随机整数

# 6.uniform(a, b)
print(r.uniform(5, 10)) # return [5, 1O] 区间中的随机小数

# 7.choice(seq)
list = [56, 'hello', [1, 2]]
print(r.choice(list)) # return list 中的随机一个元素

# 8.shuffle(seq)
r.shuffle(list)
print(list) # 将 list 中的元素打乱并返回 -- 注：shuffle 是基于原序列自动打乱，进行赋值操作会 return None

# 9.sample(pop, k)
print(r.sample(list, 2)) # 随机从 list 中选取 2 个元素，并以列表的形式返回