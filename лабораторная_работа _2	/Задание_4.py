#number of unique numbers
z = []
for i in range(5):
    a = int(input("введите число: "))
    z.append(a)

z = set(z)
print(f"количество уникальных номеров равно {len(z)}")





