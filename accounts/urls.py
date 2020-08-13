from django.urls import path
from . import views

# アプリ名を記述
app_name = 'accounts'

# ここの配列の中にルーティングを書いていきます。
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),# ユーザー追加のパスを追記
    path('<str:username>/', views.AccountDetailView.as_view(), name='userDetail'),  #ユーザー詳細画面へのパスを追記
    path('icon/edit/', views.IconEdit.as_view(), name='icon_edit'),
]