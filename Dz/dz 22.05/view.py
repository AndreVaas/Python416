def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:

    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        print("Действия со статьями")
        print("1 - Добавление фильмов"
              "\n2 - Каталог фильмов"
              # "\n3 - Просмотр определенного фильма"
              # "\n4 - Удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите действия: ")
        print("=" * 50)
        return user_answer

    @add_title("Создание статьи:")
    def add_user_article(self):
        dict_article = {
            "Название фильма ": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска ": None,
            "длительность ": None,
            "студия ": None,
            "актеры ": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} фильма: ")
        print("=" * 50)
        return dict_article

    def show_all_article(self, articles):
        print(" Каталог фильмов: ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}, {article}")
        print("=" * 50)
