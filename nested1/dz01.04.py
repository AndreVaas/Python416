import os.path

# Файлы в папке nested1: Test.txt,Text.txt, text2.txt, text3.txt, text5.txt

file = input("Укажите имя файла:")
file_directory = r"C:\Users\AndreyVasilev\Desktop\python\nested1"
for root, dirs, files in os.walk(file_directory):
    if file in files:
        path_parts = root.split(os.sep)
        two_dirs = "/".join(path_parts[-2:]) if len(path_parts) >= 2 else root
        print(f"{file} ({two_dirs}) "
              f"- last access time {os.path.getatime(file)} sec.")
        break
    else:
        print("Данного файла не существует!")
        break


