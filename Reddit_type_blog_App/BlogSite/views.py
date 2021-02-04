from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
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



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)




class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'blog_list_query'
    template_name = 'BlogSite/filtered_posts.html'

    def get_queryset(self): 
        query = self.request.GET.get('searchq')               ## 'name' from searchbar input tag

        return Post.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(Category__icontains=query)
        )


# def article_overview(request):
#     if request.method == 'GET':
#         search = request.GET.get('searchq')
#         post39 = Post.objects.all().filter(title=search)

#         return redirect('article_overview', post39='post39')
        
#         # return render(request, 'BlogSite/article_overview.html', {'post39':post39})
#     else:
#         return HttpResponse(request, "Hey Not found Anything!!")
