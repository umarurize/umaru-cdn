# 需求，目标吃5个苹果，吃完第三个吃饱了
# 即第4第5个不吃了，循环不执行
i = 1
while i <= 5:
    if i == 4:
        print(f'一共吃了{i-1}个苹果，吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
