
values = list()
for i in range(20):
    if i % 3 == 0:
        values.append(i)
        print("3::::", i)
    elif i % 4 == 0:
        values.pop()
        print("4::::",i)

print(values)
