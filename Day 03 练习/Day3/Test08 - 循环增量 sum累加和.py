
i = 1

sum = 0  # ’框‘ 变量，一定不要放入循环体 While 中

while i <= 100:
    # sum = 0， 放在这，每循环一次，sum = 0 就会将前一个 sum 覆盖掉
    sum += i

    i += 1 #一定要缩进，循环增量

print(f'sum = {sum}')