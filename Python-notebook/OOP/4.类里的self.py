'''
类里的 self
    self 指的是调用该函数的对象
'''


class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)


haier = Washer()
print(haier) # 返回对象所处的内存地址

haier.wash() # 返回 '能洗衣服’，和由 self 打印的内存地址

# 总结：因为打印 self 和打印对象返回的内存地址相同，说明 self 指的是调用该函数的对象
