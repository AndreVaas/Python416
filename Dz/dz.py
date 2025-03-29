d = {
    "John": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694
    }, "Tom": {
        "N": 4832,
        "S": 6786,
        "E": 4737,
        "W": 3612
    }, "Anne": {
        "N": 5239,
        "S": 4802,
        "E": 5820,
        "W": 1859
    }, "Fiona": {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451
    },
}
for x in d:
    print(x)
    for y in d[x]:
        print("\t", y, ": ", d[x][y], sep="")

name = input("Введите имя: ")
region = input("Введите регион (N, S, E, W): ")
if name in d and region in d[name]:
    if name != 1
    print("Текущий объем продаж:", d[name][region])
    new_value = int(input("Введите новое значение: "))
    d[name][region] = new_value
    print("Новые данные по продажам. Имя:", name, ":", d[name])
else:
    print("Ошибка: Неверное имя или регион")