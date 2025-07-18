from django.forms import ModelForm
from blog.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        labels = {
            'title': 'Название книги',
            'description': 'Отзыв',
        }
