import random
computer = random.randint(1,3)
print(f'computer = {computer}')

Nick = int(input('请输入您的招式（1：石头；2：剪刀；3：布）：'))
if Nick == 1 and computer == 2 or Nick == 2 and computer == 3 or Nick == 3 and computer == 1:
    print('恭喜你获得了胜利')
elif Nick == 1 and computer == 3 or Nick == 3 and computer == 2 or Nick == 2 and computer == 1:
    print('真遗憾，你这次输了')
else :
    print('平局，再来！')
