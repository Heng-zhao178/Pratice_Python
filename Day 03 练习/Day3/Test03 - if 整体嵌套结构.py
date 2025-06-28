age = int(input('请输入你的年龄：'))

if 0<= age <= 150: # 规定输入数据的合理范围

    if age >= 60:
        print('经鉴定，你是一位老人')
    elif age >= 30:
        print('经鉴定，你是一位中年人')
    elif age >= 20:
        print('经鉴定，你是一位成年人')

    else: # 上述条件均不成立
        print('对不起，您年龄不符，不能进行测试')
else:
    print('您的年龄不在合理范围内')


