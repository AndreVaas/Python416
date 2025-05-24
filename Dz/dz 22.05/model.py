class Article:
    def __init__(self, title, genre, director, year_of_release, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title}({self.director})"


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_article(self):
        return self.articles.values()
