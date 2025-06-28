name = '玛丽亚'

# 从右往左，把 变量值 放进 变量名 里


# 1.整型数据 int
number1 = 999
# print(f'Number1 is {number1}')
# print('Number1 is {number1}')

print(f'number1 = {number1}, type(number1)={type(number1)}')

# f ' + {变量名name}'  输出 “变量名name” 所对应的数据 “玛丽亚”




# 2. 浮点型 float
num2 = 66.6

print(f'num2 = {num2}, type(num)={type(num2)}')





# 3.bool
is_visited =  True #False
print(f'is_visited = {is_visited}, type(is_visited)={type(is_visited)}')


# 4.字符串类型  string  str
name1 = '玛丽亚'
name2 = "玛丽亚"
name3 = '''玛丽亚'''
print(f'name1 = {name1}, type(name1)={type(name1)}')


# 5.列表 list
names = ['张三','李四','王五','Lisa']
print(f'names = {names}, type(names)={type(names)}')



# 6.元组 tuple
names = ('张三','李四','王五','Lisa')
print(f'names = {names}, type(names)={type(names)}')


# 7.集合 set
names = {'张三','李四','王五','Lisa','王五'}
print(f'names = {names}, type(names)={type(names)}')

name1 = '玛丽亚'
name1 = 'Mary'  #会覆盖掉前一个数据 ’玛丽亚‘

print(f'name1 = {name1}, type(name1)={type(name1)}')


# 8.字典 dict
stu_dict = {'stu_id':'1001', 'name':'张三','age':18, 'score':100}
print(f'stu_dict = {stu_dict}, type(stu_dict)={type(stu_dict)}')