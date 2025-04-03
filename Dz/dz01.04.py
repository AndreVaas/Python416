import os.path
import time

# path1 = r"C:\Users\AndreyVasilev\Desktop\python\nested1\text3.txt"
# p = os.path.exists(path1)
# if p == True:
#     print(os.path.basename(path1), "("+os.path.dirname(path1)+")", "last access file - ", os.path.getatime(path1),
#     "sec")
# else:
#     print("Данного файла не существует!")

# Вариант 2
path1 = input("Укажите адрес файла: ")
p = os.path.exists(path1)
if p == True:
    print(os.path.basename(path1), "("+os.path.dirname(path1)+")", "- last access file ", os.path.getatime(path1),
          "sec.")
else:
    print("Данного файла не существует!")

    # C:\Users\AndreyVasilev\Desktop\python\nested1\text3.txt
    # C:\Users\AndreyVasilev\Desktop\python\Word\w.txt