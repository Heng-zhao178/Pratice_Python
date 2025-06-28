
money = 100
withdraw_money = int(input('请输入您的本次取款金额：'))

if withdraw_money <= money:
    money -= withdraw_money
    print(f'您的银行卡余额为{money}元')
    print(f'吐出钞票：{withdraw_money}元')
else:
    print('您的银行卡余额不足')

choice = input('请问您是否需要退卡？（y退卡，n继续执行其他操作）：')
if choice == 'y' or choice == 'Y':
    print('请收好您的卡片，感谢您的使用，再见')
else:
    print('执行其他操作……')
