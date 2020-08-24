from django.db import models
from accounts.models import User


# Create your models here.
class Post(models.Model):
    # 外部キーとしてaccounts.Userと紐付けするためのカラム
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    salon = models.ForeignKey(
        'posts.Salon', on_delete=models.SET_NULL, null=True)
    adviser = models.ForeignKey(
        'posts.Adviser', on_delete=models.SET_NULL, null=True)
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

class Salon(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    tel = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.CharField(max_length=8, blank=True, null=True)
    address1 =  models.CharField(max_length=6, blank=True, null=True)
    address2 = models.CharField(max_length=20, blank=True, null=True)
    address3 = models.CharField(max_length=20, blank=True, null=True)
    salon_url  = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name

class Adviser(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    salon = models.ForeignKey('posts.Salon', on_delete=models.SET_NULL, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name

class Useradviser(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    adviser = models.ForeignKey(
        'posts.Adviser', on_delete=models.CASCADE)
