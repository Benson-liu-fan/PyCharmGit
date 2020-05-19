a = input()
if a[0:].isnumeric() == True:
    if a[0] != "-":
        print(a[::-1])
    else:
        a = a[1:][::-1]
        a = int(a)
        a = -a
        print(a)
elif a[1:].isnumeric() == True:
    a = a[1:][::-1]
    a = int(a)
    a = -a
    print(a)
else:
    print("输入有误！")
