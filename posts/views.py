from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View   # 追加
from django.http import HttpResponse

from .forms import PostForm, SalonAddForm, AdviserAddForm

from .models import Post, Like, Comment, Salon, Adviser, Useradviser

# 投稿画面
class New(CreateView):
    model = Post
    # 使うためテンプレートの指定
    template_name = 'posts/new.html'
    # 使うformクラスの指定
    form_class = PostForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('posts:index')

    def get_initial(self):
        return {'author': self.request.user}
    # 入力に問題がない場合現在ログインしているアカウントを投稿者として登録するための処理
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salon_list'] = Salon.objects.all()
        return context
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(New, self).form_valid(form)

def ajax_get_adviser(request):
    pk = request.GET.get('pk')
    # pkパラメータがない、もしくはpk=空文字列だった場合は全カテゴリを返しておく。
    if not pk:
         adviser_list = Adviser.objects.all()

    # pkがあれば、そのpkでadviserを絞り込む
    else:
         adviser_list = Adviser.objects.filter(salon__pk=pk)

    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる。
    adviser_list = [{'pk': adviser.pk, 'name': adviser.name} for adviser in adviser_list]

    # JSONで返す。
    return JsonResponse({'adviserList': adviser_list})


class PostUpdateView(UpdateView):
    # 使うためテンプレートの指定
    template_name = 'posts/post_update.html'
    # 使うformクラスの指定
    model = Post
    form_class = PostForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('posts:index')

class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    fields = ("picture", "picture2", "picture3", "text", "author", "adviser", "salon", "created_at")

class PostDeleteView(DeleteView):
    template_name = 'posts/post_delete.html'
    model = Post
    success_url = reverse_lazy('posts:index')

# 投稿一覧
class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    #  最大表示件数を設定しています 今回は100件
    paginate_by = 100
    # データを取得するときに行う処理を記述できる今回は投稿日を降順で並べる様にした
    queryset = Post.objects.order_by('created_at').reverse()
  #   以下追加
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        like_list = {}
        comment_list = {}
        # すでに取得されている投稿リストを一件づつ取り出す
        for post in context['post_list']:
            # 取り出したものから「いいね!」を探してlike_listに格納する
            like_list[post.id] = Like.objects.filter(post=post)
        context['like_list'] = like_list
        return context

class Likes(View):
    model = Like
    slug_field = 'post'
    slug_url_kwarg = 'postId'

    def get(self, request, postId):
        post = Post.objects.get(id=postId)
        like = Like.objects.filter(author=self.request.user, post=post)
        like_list = {}
        # 過去にいいねを押しているのか
        if like.exists():
            # いいねされていれば消す
            like.delete()
        else:
            # いいねされていなければ追加する
            like = Like(author=self.request.user, post=post)
            like.save()
        like_list[post.id] = Like.objects.filter(post=post)
        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'post': post
        })
class AddComment(View):
    def post(self, request, postId):
        like_list = {}
        comment_list = {}

        post = Post.objects.get(id=postId)
        text = request.POST["comment"]

        comment = Comment(author=self.request.user, post=post, text=text)
        comment.save()

        like_list[post.id] = Like.objects.filter(post=post)
        comment_list[post.id] = Comment.objects.filter(post=post)
        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'comment_list': comment_list,
            'post': post
        })
def menu(request):
    template_name = 'posts/menu.html'
    return render(request,'posts/menu.html',{})

class SalonAddView(CreateView):
    template_name = 'posts/salon_add.html'
    # 使うformクラスの指定
    form_class = SalonAddForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('posts:salonlist')

class SalonListView(ListView):
    model = Salon
    queryset = Salon.objects.order_by('id')
class SalonUpdateView(UpdateView):
    model = Salon
    template_name = 'posts/salon_update.html'
    form_class = SalonAddForm

    def get_success_url(self):
        return reverse_lazy('posts:salonlist')

class AdviserAddView(CreateView):
    template_name = 'posts/adviser_add.html'
        # 使うformクラスの指定
    form_class = AdviserAddForm
        # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('posts:adviserlist')

class AdviserListView(ListView):
    model = Adviser
    queryset = Adviser.objects.order_by('id')

class AdviserUpdateView(UpdateView):
    model = Adviser
    template_name = 'posts/adviser_update.html'
    form_class = AdviserAddForm

    def get_success_url(self):
        return reverse_lazy('posts:adviserlist')

    def get_form(self):
        form = super(AdviserUpdateView, self).get_form()
        return form
