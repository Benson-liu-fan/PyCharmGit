import random
x = random.randint(0,30)
n = input()
m = 0
while n.isalpha() == False:            #判断是否为字符
    m += 1
    if eval(n) > x:
        print("遗憾，太大了！")
    elif eval(n) < x:
        print("遗憾，太小了！")
    else:
        print("预测{}次，你猜中了！".format(m))
        break
    n = input()
    if n.isalpha() == True:
        print("请输入一个数字吧！")
        break
else:
    print("请输入一个数字！")
