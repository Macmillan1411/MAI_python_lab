
def big_small_switch(lst):
    big = max(lst)
    small = min(lst)

    x = lst.index(big)
    y = lst.index(small)

    lst[x],lst[y] = small,big

    return lst
