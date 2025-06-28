name ='小明'
print(f'name = 我的名字叫{name}，请多多关照！')


name ='小美'
print(f'name = 我的名字叫{name}，请多多关照！')

print(name)
print('name')


name='小明'
age=18
print(f'我的名字叫%s，今年%d岁，请多多关照！'%(name,age))

student_nu = '000001' #整型数值不能以0开头
print(f'我的学号是 {student_nu}')

student_nu = 1 #整型数值不能以0开头
print('我的学号是 %06d' % student_nu )

price=9.00
weight=5.00
money= price * weight
print(f'苹果单价%.1f元/斤，购买了%.1f斤，需要支付%.2f元' % (price,weight,money))


scale = 10.00
print('数据比例是%.2f%%' % (scale,))
print('数据比例是%.2f%%' % scale)
