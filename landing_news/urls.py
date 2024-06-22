from django.urls import path
from landing_news.views import News_list , News_detail, News_create, News_update , News_delete , about

app_name = 'landing_news'

urlpatterns = [
    path('', News_list.as_view(), name='landing'),
    path('detail/<pk>', News_detail.as_view(), name='new_detail'),
    path('create/', News_create.as_view(), name='new_create'),
    path('update/<pk>', News_update.as_view(), name='new_update'),
    path('delete/<pk>', News_delete.as_view(), name='new_delete'),
    path('delete/<pk>', News_delete.as_view(), name='new_delete'),
    path('sobre_mi/', about, name='about'),
]

