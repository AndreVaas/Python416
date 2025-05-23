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
        # (" Ввод пользовательских данных ".center(50,
        #                                               "="))
        print("Действия со статьями")
        print("1 - Создание статьи"
              "\n2 - Просмотр статей"
              "\nq - выход из программы")
        user_answer = input("Выберите действия: ")
        print("=" * 50)
        return user_answer

    @add_title("Создание статьи:")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        # print(" Создание статьи: ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        print("=" * 50)
        return dict_article

    def show_all_article(self, articles):
        print(" Список статей: ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}, {article}")
        print("=" * 50)
