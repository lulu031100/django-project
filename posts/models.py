from django.db import models
from accounts.models import User


# Create your models here.
class Post(models.Model):
    # 外部キーとしてaccounts.Userと紐付けするためのカラム
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    #  画像を登録するためのカラム
    picture = models.ImageField(
        upload_to="image/posts/", blank=False, null=False)
    # 写真のコメントを追加するためのカラム
    text = models.TextField(blank=True)
    # 投稿日を持つためのカラム
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
# いいね機能のため

class Like(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
# コメント
class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)