from django import template
from django.utils.safestring import mark_safe
from ..models import Like
register = template.Library()

@register.filter(name='get_likes')
def get_likes(like_list, key):
    text = ""
    if key in like_list:
        text = ""
        for like in like_list[key]:
            text += f"{like.author.username}, "
            text += "がいいねしました"
    return text

@register.filter(name='is_like')
def is_like(post, user):
    if Like.objects.filter(author=user, post=post).exists():
        return mark_safe(f"<button class=\"like\" id=\"{post.id}\" type=\"submit\"><i class=\" fas fa-heart\"></i></button>")
    else:
        return mark_safe(f"<button class=\"like\" id=\"{post.id}\" type=\"submit\"><i class=\" far fa-heart\"></i></button>")

@register.filter(name='get_comment_list')
def get_comment_list(comment_list, key):
    text = ""
    key = str(key)
    if key in comment_list:
       for comment in comment_list[key]:
            text += f"@{comment.author.username}: {comment.text}<br>"
    return mark_safe(text)