import itertools as it
import pandas as pd


# 产生组合
def get_all(n = 34):
    all = it.combinations([i for i in range(1, n, 1)], 6)
    return all

# 龙头单双
def count_dragon_head(all):
    result = []
    for a in all:
        i = a[0]
        if i % 2 == 0:
            result.append([a, 0])
        else:
            result.append([a, 1])
    result = pd.DataFrame(result, columns=['Combinations', 'dragon'])
    return result


# 凤尾单双
def count_phoenix_tail(all):
    result = []
    for a in all:
        i = a[-1]
        if i % 2 == 0:
            result.append([a, 0])
        else:
            result.append([a, 1])
    result = pd.DataFrame(result, columns=['Combinations', 'phoenix'])
    return result

# 三区龙虎和
def count_three_terms(all):
    count = 0
    result = []
    for a in all:
        one = 0
        two = 0
        three = 0
        for i in a:
            if i <= 11:
                one += 1
            elif i <= 22:
                two += 1
            else:
                three += 1
        count += 1
        # 1&2
        if one > two:
            result.append([a, 0])
        elif one < two:
            result.append([a, 1])
        else:
            result.append([a, 2])
    result = pd.DataFrame(result, columns=['Combinations', '1&2'])
    return result

# 连号号码数
def count_continue(all):
    result = []
    for a in all:
        tmp = -1
        num = 1
        for i in a:
            if tmp == -1:
                tmp = i
            else:
                if i-tmp == 1:
                    num += 1
                tmp = i
        result.append([a, num])

    result = pd.DataFrame(result, columns=['Combinations', 'nums'])
    result.to_csv("continue_nums.csv", index=False)

all = get_all()
a = count_dragon_head(all)
all = get_all()
b = count_phoenix_tail(all)
all = get_all()
c = count_three_terms(all)

# merge all result to one excel file
result = a.merge(b, on=['Combinations'], how='left')
result = result.merge(c, on=['Combinations'], how='left')

# split dataframe to four pages
#apprix_1 = result.iloc[:300000, :]
#apprix_2 = result.iloc[300000:600000, :]
#apprix_3 = result.iloc[600000:900000, :]
apprix_4 = result.iloc[900000:, :]

#apprix_1.to_excel("two-color-balls.xlsx", sheet_name='1', index=False)
#apprix_2.to_excel("2.xlsx", sheet_name='2', index=False)
#apprix_3.to_excel("3.xlsx", sheet_name='3', index=False)
apprix_4.to_excel("4.xlsx", sheet_name='4', index=False)
'''
with pd.ExcelWriter("two-color-balls.xlsx", mode='a') as writer:
    apprix_2.to_excel(writer, sheet_name='2', index=False)
with pd.ExcelWriter("two-color-balls.xlsx", mode='a') as writer:
    apprix_3.to_excel(writer, sheet_name='3', index=False)
with pd.ExcelWriter("two-color-balls.xlsx", mode='a') as writer:
    apprix_4.to_excel(writer, sheet_name='4', index=False)

'''
