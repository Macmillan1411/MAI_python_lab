def bigger(lst):
    bglst = []
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            bglst.append(lst[i + 1])
    return bglst

print(bigger([1,2,3,4,5,4,0,7,4,6,3,2,11]))