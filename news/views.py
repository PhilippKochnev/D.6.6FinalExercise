from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from .models import Category


# Категории отражаются на главной странице
class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'flatpages/news/home.html'
    context_object_name = 'category'


# Список новостей отражается на своей странице


class PostList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'flatpages/news/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['next_sale'] = "Все актуальные новости у нас!"
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'flatpages/news/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'





