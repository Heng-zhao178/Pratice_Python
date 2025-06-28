
# 死循环 - 穷举法


# i = 2   # 循环变量
#
# while True: # 循环条件 - 死循环，停不下来
#
#     if i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1:
#         print(f'i = {i}')
#
#     i += 1 # 循环增量

i = 2

while True:  # 循环条件 - 死循环

    if i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1 and i % 7 == 1:
        print(f'i = {i}')
        break # 遇到break，循环立刻停止

    i += 1  # 循环增量


