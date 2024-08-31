# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog/post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def post_edit(request, pk=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')  # Redirige a la lista de posts después de guardar
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})
