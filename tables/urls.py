from django.urls import path
from tables.views import (
Player_list , Player_detail, Player_create, Player_update , Player_delete,
Tables_list , Table_detail , Table_create , Table_update , Table_delete
)

app_name = 'tables'

urlpatterns = [
    path('players/', Player_list.as_view(), name='players_list'),
    path('player/detail/<pk>', Player_detail.as_view(), name='player_detail'),
    path('player/create/', Player_create.as_view(), name='player_create'),
    path('player/update/<pk>', Player_update.as_view(), name='player_update'),
    path('player/delete/<pk>', Player_delete.as_view(), name='player_delete'),
]


urlpatterns  += [
    path('tables/', Tables_list.as_view(), name='tables_list'),
    path('table/detail/<pk>', Table_detail.as_view(), name='table_detail'),
    path('table/create/', Table_create.as_view(), name='table_create'),
    path('table/update/<pk>', Table_update.as_view(), name='table_update'),
    path('table/delete/<pk>', Table_delete.as_view(), name='table_delete'),
]