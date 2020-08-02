"""techpitgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # 修正  urlsのファイルを読み込むincludeを追加
from django.views.static import serve  # 後に使うviewsのファイルを追加
from django.conf import settings  # プロジェクトの設定を読み込むプログラムを呼び出す部分を追加


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # 追加
    path('accounts/', include('accounts.urls')),  # accountsアプリのurlsを読み込む処理を追加
    path('', include('posts.urls')),  # postsのurls.pyへのパスを追加
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),  # プロジェクト設定を呼び出して画像のためのパス設定を追加
]