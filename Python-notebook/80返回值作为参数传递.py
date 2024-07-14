def test1():
    return 50
    

def test2(num): # num 作为形参
    print(num) 
    
    
# 1.调用 test1 并用变量保存其返回值
result = test1()

test2(result) # 返回 50，验证了返回值可以作为参数传递

