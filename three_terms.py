import itertools as it
import pandas as pd
def get_all():
    all = it.combinations([i for i in range(1, 34, 1)], 6)
    return all
    result = []
    for a in all:
        result.append(list(a))
    result = pd.DataFrame(result, columns=[1, 2, 3, 4, 5, 6])
    result.to_csv("all.csv", index=False)

def count_even_odd_equal(all):
    count = 0
    even_large = 0
    odd_large = 0
    equal = 0
    for a in all:
        even = 0
        odd = 0
        for i in a:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        if even > odd:
            even_large += 1
        elif even < odd:
            odd_large += 1
        else:
            equal += 1
        count += 1
    return odd_large, even_large, equal, count

def count_large_small_equal():
    count = 0
    large_large = 0
    small_large = 0
    equal = 0
    for a in all:
        small = 0
        large = 0
        for i in a:
            if i >= 17 == 0:
                large += 1
            else:
                small += 1
        if large > small:
            large_large += 1
        elif large < small:
            small_large += 1
        else:
            equal += 1
        count += 1
    return large_large, small_large, equal, count

def count_three_terms(all):
    count = 0
    one_and_two = [0, 0, 0]
    one_and_three = [0, 0, 0]
    two_and_three = [0, 0, 0]
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
            one_and_two[0] += 1
        elif one < two:
            one_and_two[1] += 1
        else:
            one_and_two[2] += 1
        # 1&3
        if one > three:
            one_and_three[0] += 1
        elif one < three:
            one_and_three[1] += 1
        else:
            one_and_three[2] += 1
        # 2&3
        if two > three:
            two_and_three[0] += 1
        elif two < three:
            two_and_three[1] += 1
        else:
            two_and_three[2] += 1
    return one_and_two, one_and_three, two_and_three, count


def count_gap(all, start, end):
    count = 0
    num = 0
    for a in all:
        count += 1
        maxnum = max(a)
        minnum = min(a)

        if (maxnum-minnum) >= start and (maxnum-minnum) <= end:
            num += 1
    return num/count


def count_continue(all):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    count = 0
    for a in all:
        count += 1
        tmp = -1
        num = 1
        for i in a:
            if tmp == -1:
                tmp = i
            else:
                if i-tmp == 1:
                    num += 1
                tmp = i
        dic[num] += 1

    return dic, count

count = 0
#all = pd.read_csv("all.csv", index_col=False)
all = get_all()
#print(count_continue(all))
result, count_to = count_continue(all)
total = 0
for i in result:
    total += result[i]
    print(result[i]/count_to)
print(total)
