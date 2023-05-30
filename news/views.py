from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from .models import Category
from .filters import PostFilter


# Категории отражаются на главной странице
class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'flatpages/news/home.html'
    context_object_name = 'category'


# Список новостей отражается на своей странице


class PostList(ListView):
    model = Post
    ordering = 'header'
    template_name = 'flatpages/news/news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


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





