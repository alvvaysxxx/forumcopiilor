from datetime import timezone, datetime, timedelta
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils import timezone

from .forms import *
from .models import Post, ChangeLogPost


# Create your views here.


class PostView(View):
    def get(self, request):
        posts = Post.objects.all().annotate(comment_count=Count('comments')).order_by('-date')
        return render(request, 'forum/post.html', {'post_list': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = datetime.now()
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})



class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        comments = reversed(list(post.comments_set.all()))
        return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})


class AddComment(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.date = datetime.now()
            form.save()
            return redirect(f'/{pk}')
        else:
            form = CommentsForm()

def AboutPage(request):
    return render(request, 'forum/about.html')

def RulesPage(request):
    return render(request, 'forum/rules.html')

def post_wait(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'forum/post_wait.html', {'post_list': posts})

def changelog(request):
    changelog_posts = ChangeLogPost.objects.all().order_by('-date_changelog')
    return render(request, 'forum/changelog.html', {'changelog_list': changelog_posts})