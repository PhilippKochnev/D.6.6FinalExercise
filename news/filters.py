from django_filters import FilterSet
from .models import Post


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            # 'category': ['icontains'],
            # 'rating': [
            #     'lt',  # рейтинг должен быть меньше или равна указанной
            #     'gt',  # рейтинг должен быть больше или равна указанной
            # ],
        }
