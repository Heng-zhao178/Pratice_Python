           #   注意缩进，缩进不同，含义不同

# 1. 循环变量
i = 1

count = 0 # 也不要写进循环体中

# 2. 循环体
while i <= 30:
    # 2.1. 条件体
    if i % 3 == 0:
        count += 1
        print(i, end='\t')

    i += 1 #不属于条件体，只缩进一次

# 3. 循环增量
print(f'count = {count}')