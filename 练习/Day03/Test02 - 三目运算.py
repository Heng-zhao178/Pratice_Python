
num1 = int(input('请输入第一个整型数值：'))
num2 = int(input('请输入第二个整型数值：'))
num3 = int(input('请输入第三个整型数值：'))


second_max = num1 if num1 > num2 else num2
max = second_max if second_max > num3 else num3
# 条件成立，结果左边； 条件不成立，结果右边
print(f'max = {max}')
