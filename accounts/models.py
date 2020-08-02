from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# AbstractUser: Djangoが用意しているUserモデルを継承する
class User(AbstractUser):
    # アイコンを画像を保存できるImageFieldとして定義する
    icon = models.ImageField(upload_to="image/", blank=True, null=True)

    # 作成を成功したら'ginstagram:profile'と定義されているURLに飛ぶ
    def get_absolute_url(self):
        return reverse(
            'ginstagram:profile', kwargs={'username': self.username})
