

# 1.   for + range 用于 ‘知道循环次数’ 的循环，首尾确定
sum = 0
range(1, 101, 1)
for i in range(1, 101, 1):
    # print(i, end='\t')
    sum += i
print(f'sum = {sum}')



print('-' * 50)



# 2.  while循环 一般都是 While True + break，不知道循环次数
Sum = 0
i = 1
while i < 101:
                 # print(i, end='\t')
    Sum += i     # 先写 Sum，再写 i
    i += 1       # 循环增量 一定不能忘记，也要记住位置
print(f'Sum = {Sum}')