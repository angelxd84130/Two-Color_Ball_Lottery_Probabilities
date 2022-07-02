import itertools as it
import pandas as pd
# 蓝球
# 产出组合
def get_all():
    return [i for i in range(1, 17, 1)]

# 大/小
def count_large_small(all):
    large = 0
    count = 0
    for a in all:
        count += 1
        if a >= 9:
            large += 1
    return large/count, (count-large)/count

# 单/双
def count_even_odd(all):
    even = 0
    count = 0
    for a in all:
        count += 1
        if a % 2 == 0:
            even += 1
    return (count - even) / count, even / count

# 质/合
def count_prim(all):
    prim_num = [1, 2, 3, 5, 7, 11, 13]
    prim = 0
    count = 0
    for a in all:
        count += 1
        if a in prim_num:
            prim += 1
    return prim / count, (count - prim) / count

# 选号
def count_select_num(all):
    return 1/len(all)

# 五行-金木水火土
def count_blue_five_types(all):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    count = 0
    for a in all:
        count += 1
        i = a
        if i in [9, 10]:
            one += 1
        elif i in [3, 4, 15, 16]:
            two += 1
        elif i in [1, 12, 13]:
            three += 1
        elif i in [6, 7]:
            four += 1
        elif i in [2, 5, 8, 11, 14]:
            five += 1
        else:
            print("error value", i)

    return (one/count, two/count, three/count, four/count, five/count)

''' test function '''
all = get_all()
print(count_prim(all))
