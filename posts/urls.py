from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'posts'

urlpatterns = [
    path('new/', login_required(views.New.as_view()), name='new'),
    path('api/adviser/get/', views.ajax_get_adviser, name='ajax_get_adviser'),  # これ
    path('postupdate/<int:pk>', login_required(views.PostUpdateView.as_view()), name='postupdate'),
    path('postdetail/<int:pk>/', views.PostDetailView.as_view(), name='postdetail'),
    path('postdelete/<int:pk>', views.PostDeleteView.as_view(), name='postdelete'),
    path('', login_required(views.Index.as_view()), name='index'),
    path('menu/', login_required(views.menu), name='menu'),
    path('<postId>/like/', login_required(views.Likes.as_view()), name='like'),
    path('<postId>/comment/', login_required(views.AddComment.as_view()), name='comment'),
    path('salonadd/', views.SalonAddView.as_view(), name='salon_add'),
    path('salonlist/', views.SalonListView.as_view(), name='salonlist'),
    path('<int:pk>/salonupdate', views.SalonUpdateView.as_view(), name='salon_update'),
    path('adviseradd/', views.AdviserAddView.as_view(), name='adviser_add'),
    path('adviserlist/', views.AdviserListView.as_view(), name='adviserlist'),
    path('<int:pk>/adviserupdate', views.AdviserUpdateView.as_view(), name='adviser_update'),
]