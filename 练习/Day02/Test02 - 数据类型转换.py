int,
float
str

num1 = '10'
num2 = '30'

result = num1 + num2
print(f'type(num1)={type(num1)}, type(num2)={type(num2)}')
print(f'result={result}') #字符串类型数据相加，就是拼接数据 str

result = int(num1 + num2)
print(f'result={result}')

n1 = int(num1)
n2 = int(num2)
result = n1 + n2
print(f'type(n1)={type(n1)}, type(n2)={type(n2)}')
print(f'result={result}') # int+int 就是数学运算


f1 = 66.69
f2 = 889.56
result = f1 + f2
print(f'result={result}')

i1 = int(f1)
i2 = int(f2)    # int 就是去掉小数点，去尾法，不是四舍五入
result = i1 + i2
print(f'result={result}') #所以结果会丢失精度

n1 = 20
n2 = 45
f1 = float('%.3f' %(n1))
f2 = float('%.3f' %(n2))
result = f1 + f2
print(f'result={result}')





