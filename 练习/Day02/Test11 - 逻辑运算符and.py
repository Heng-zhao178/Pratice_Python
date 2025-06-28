
gender = input('请输入你的性别：')
age = int(input('请输入你的年龄： ')) #转换为 int整型数值

result = gender == '男' and age >= 18
print(f'result = {result}')

