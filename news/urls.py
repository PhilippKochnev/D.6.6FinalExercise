from django.urls import path
# Импортируем созданное нами представление
from .views import CategoryList
from .views import PostList, PostDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('', CategoryList.as_view(), name='home'),
      path('news/', PostList.as_view(), name='news'),
      path('news/<int:post_id>', PostDetail.as_view(), name='post'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


