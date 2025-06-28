
T_shirt = float(input('请输入T_shirt的单价：'))
Pants = float(input('请输入Pants的单价： '))

T_shirt_count = int(input('你买了几件T_shirt？ '))
Pants_count = int(input('你买了几件Pants？ '))

normal_price = T_shirt*T_shirt_count + Pants*Pants_count
print(f'normal_price={normal_price}')

discount = 0.88
discount_price = discount * normal_price
print(f'discount_price={discount_price}')