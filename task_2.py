def unique():
    lst = []
    for i in range(10):
        num = eval(input("введите число: "))
        lst.append(num)
    return len([i for i in lst if i == 0])








print(f"количество чисел = 0 равно {unique()}")
