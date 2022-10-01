
l = []
for i in range(10):
    num = eval(input("введите число: "))
    l.append(num)

print(f"количество чисел = 0 равно {len([i for i in l if i == 0])}")