from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
    return render(request, 'BlogSite/post_edit.html', {'form': form})




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




# def article_overview(request):
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         articles = Post.objects.all().filter(title__icontains=search_term) 

#     # articles = Post.objects.all()

#     return render(request, 'BlogSite/overview.html', {'articles' : articles, 'search_term': search_term })    



def article_overview(request):
    if request.method == 'GET':
        search = request.GET.get('searchq')
        post39 = Post.objects.all().filter(title=search)

        return redirect('article_overview', post39='post39')
        
        # return render(request, 'BlogSite/article_overview.html', {'post39':post39})
    else:
        return HttpResponse(request, "Hey Not found Anything!!")





# class SearchView(ListView):
# model = Article
# template_name = 'search.html'
# context_object_name = 'all_search_results'

# def get_queryset(self):
#     result = super(SearchView, self).get_queryset()
#     query = self.request.GET.get('search')
#     if query:
#         postresult = Article.objects.filter(title__contains=query)
#         result = postresult
#     else:
#         result = None
#     return result