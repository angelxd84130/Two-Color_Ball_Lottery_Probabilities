import itertools as it
import pandas as pd
def get_all(n = 34):
    all = it.combinations([i for i in range(1, n, 1)], 6)
    return all


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
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
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


def count_three_zones(all):
    count = 0
    dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for a in all:
        num = 0
        for i in a:
            if i <= 11:
                num += 1
        dic[num] += 1
        count += 1
    return dic, count

def count_dragon_head(all):
    even = 0
    count = 0
    for a in all:
        for i in a:
            if i % 2 == 0:
                even += 1
            break
        count += 1
    return (count-even)/count, even/count

def count_dragon_select(all):
    dic = {}
    count = 0
    for a in all:
        for i in a:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            break
        count += 1
    return dic, count


def count_tiger_tail(all):
    even = 0
    count = 0
    for a in all:
        i = a[-1]
        if i % 2 == 0:
            even += 1
        count += 1
    return (count-even)/count, even/count

def count_tiger_select(all):
    dic = {}
    count = 0
    for a in all:
        i = a[-1]
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        count += 1
    return dic, count


def count_dead_select(all, checklist):
    count = 0
    num = 0
    for a in all:
        for i in a:
            if i in checklist:
                num += 1
                break
        count += 1


    return (count-num)/count

def count_select(all, checklist):
    length = len(checklist)
    count = 0
    num = 0
    for a in all:
        count += 1
        get = 0
        for i in a:
            if i in checklist:
                get += 1
        if get == length:
            num += 1

    return num/count

def count_red_five_types(all, n):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    count = 0
    for a in all:
        count += 1
        i = a[n-1]
        if i in [9, 10, 21, 22, 33]:
            one += 1
        elif i in [3, 4, 15, 16, 27, 28]:
            two += 1
        elif i in [1, 12, 13, 24, 25]:
            three += 1
        elif i in [6, 7, 18, 19, 30, 31]:
            four += 1
        elif i in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]:
            five += 1
        else:
            print("error value", i)

    return (one/count, two/count, three/count, four/count, five/count)



def count_red_five_types(all, n):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    count = 0
    for a in all:
        count += 1
        i = a[n-1]
        if i in [9, 10, 21, 22, 33]:
            one += 1
        elif i in [3, 4, 15, 16, 27, 28]:
            two += 1
        elif i in [1, 12, 13, 24, 25]:
            three += 1
        elif i in [6, 7, 18, 19, 30, 31]:
            four += 1
        elif i in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]:
            five += 1
        else:
            print("error value", i)

    return (one/count, two/count, three/count, four/count, five/count)


def dragon_tiger_odd(all):
    count = 0
    num = 0
    for a in all:
        if a[0]%2==1 or a[-1]%2==1:
            num += 1
        count += 1
    return num/count

def dragon_tiger_even(all):
    count = 0
    num = 0
    for a in all:
        if a[0]%2==0 or a[-1]%2==0:
            num += 1
        count += 1
    return num/count


all = get_all()

print('********')

print(count_select(all, [2,5,18,29,30]))