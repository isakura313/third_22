# нам нужно создать таблицу умножения, также, как  она была написана на тетрадках
first_arr = []

for i in range(1, 10):
    # first_arr.append(i)
    temp_arr = []
    for j in range(1,10):
        temp_arr.append(i * j)
    print(temp_arr)
# print(first_arr)

