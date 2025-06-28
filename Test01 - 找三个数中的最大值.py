
num1 = int(input('请输入第一个整型数值：'))
num2 = int(input('请输入第二个整型数值：'))
num3 = int(input('请输入第三个整型数值：'))

if num1 > num2: #条件嵌套 - 注意缩进
    if num1 > num3:
        print(f'num1是三个数中的最大值，为{num1}')
    else:
        print(f'num3是三个数中的最大值，为{num3}')
else:
    if num2 > num3:
        print(f'num2是三个数中的最大值，为{num2}')
    else:
        print(f'num3是三个数中的最大值，为{num3}')