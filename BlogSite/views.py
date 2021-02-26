from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.

def blog_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'BlogSite/blog_index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'BlogSite/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.topic = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'BlogSite/post_create.html', {'form': form})






class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'blog_list_query'
    template_name = 'BlogSite/filtered_posts.html'

    def get_queryset(self): 
        query = self.request.GET.get('searchq')               ## 'name' from searchbar input tag

        return Post.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(Category__icontains=query)
        )







def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'BlogSite/add_comment_to_post.html', {'form': form})



# @login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.temp_id)

# @login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.temp_id)





# def PostLike(DetailView):
#     post = get_object_or_404(Post, id = request.POST.get('blogpost_id'))
#     if post.likes.filter(temp_id=request.user.id).exist():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)

#     return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))