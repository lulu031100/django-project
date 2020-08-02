from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        # 使うモデルの指定です。定義したものを使います。
        model = User
        # ここではフォームで入力するフィールドを指定しています。
        fields = ("username", "password1", "password2", "icon")

    # 入力したパスワードの検証(バリデーション)を行っています
    def clean_password(self):
        # 入力されたパスワードを取得します
        password = self.cleaned_data.get('password1')
        # 数字とアルファベットが含まれているのかチェックします。
        if not re.search(r'\d', password):
            raise forms.ValidationError('数字が含まれていません')
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError('アルファベットが含まれていません')
        return password