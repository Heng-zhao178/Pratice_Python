
member = input('请问您是否为本店会员（y会员，n非会员）：')
money = int(input('请问您在本店的此次消费金额是：'))

if member == 'y' or member == 'Y':
    if money >= 200:
        print('您的本次购物将享受八折优惠')
    elif money >= 100:
        print('您的本次购物将享受九折优惠')
    else:
        print('您的本次购物不能享受折扣优惠')
else:
    if money >= 200:
        print('您的本次购物将享受九五折优惠')
    else:
        print('您的本次购物不能享受折扣优惠')