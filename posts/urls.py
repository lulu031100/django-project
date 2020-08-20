from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'posts'

urlpatterns = [
    path('new/', login_required(views.New.as_view()), name='new'),
    path('', login_required(views.Index.as_view()), name='index'),
    path('menu/', login_required(views.menu), name='menu'),
    path('<postId>/like/', login_required(views.Likes.as_view()), name='like'),
    path('<postId>/comment/', login_required(views.AddComment.as_view()), name='comment'),  # 追加
]