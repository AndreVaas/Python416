file = "res46.txt"
f = open(file, "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")

f.close()

f = open(file, "r")
read_line = f.readlines()
print(read_line)
f.close()

pos1 = int(input("Введите номер изменяемой строки:"))
pos2 = int(input("Введите номер на которую производится замена:"))

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Такой строки нет")

print(read_line)
f.close()

f = open(file, "w")
f.writelines(read_line)
f.close()