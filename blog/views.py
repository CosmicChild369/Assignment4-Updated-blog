from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth import logout

def about(request):
    return render(request, 'blog/about.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article created successfully.")
            return redirect('blog-home')
    else:
        form = ArticleForm()
    
    return render(request, 'blog/article_form.html', {'form': form})

@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Ensure that only the author can edit the article
    if request.user != article.author:
        messages.error(request, "You do not have permission to edit this article.")
        return redirect('article_detail', pk=article.pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully.")
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'blog/article_form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Ensure that only the author can delete the article
    if request.user != article.author:
        messages.error(request, "You do not have permission to delete this article.")
        return redirect('article_detail', pk=article.pk)
    
    if request.method == 'POST':
        article.delete()
        messages.success(request, "Article deleted successfully.")
        return redirect('blog-home')
    
    return render(request, 'blog/article_confirm_delete.html', {'article': article})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
    return redirect('article_detail', pk=article.pk)

@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/article_detail.html', {'article': article, 'form': form})
def custom_logout(request):
    logout(request)
    return redirect('blog-home')

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})
