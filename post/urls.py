from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>', views.detail, name='detail'),
    path('tag/<tag>', views.tag, name='tag'),
    path('board/<name>', views.board, name='board')
]   