from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

def blog(request):
    """ A view to show all products, including sorting and search queries """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/all_posts.html', context)

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'all_posts.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    """ A view to show individual product details """

    post = get_object_or_404(Post, slug = slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)