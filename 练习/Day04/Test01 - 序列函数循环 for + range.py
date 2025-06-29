



t = 3  # 一个while循环和range函数等价
while t < 92:
    print(t, end='\t')      # 水平制表符 \t
    t += 5  # 属于While循环的一部分，注意Tab



r = range(1, 11, 1)
print(f'r = {r}')

for i in range(3, 92, 5):   # 输出呈现序列 for i in rang(2, 52, 2)
    # start 开始的数值，默认0
    # stop 结束的数值，但不包含该数值
    # step 步长，默认1
    # rang(11) = range(0, 11, 1)
    print(i, end='\t') # 水平制表符 \t


for x in range(56): # = range(0, 56, 1)
    print(x, end='\t')  # 水平制表符 \t


