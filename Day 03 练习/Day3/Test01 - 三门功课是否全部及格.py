

score1 = int(input('请输入你的语文成绩：'))
result1 = score1 >= 60


score2 = int(input('请输入你的数学成绩：'))
result2 = score2 >= 60


score3 = int(input('请输入你的英语成绩：'))
result3 = score3 >= 60


result = score1 >= 60 and score2 >= 60 and score3 >= 60


if result == True:
    print('小明的三门功课全部及格')
else:
    print('小明的三门功课并没有全部及格')