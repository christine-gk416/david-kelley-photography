from django.shortcuts import render

from blog.models import Post


def index(request):
    """ A view to return the index page """
    # Display and filter blog posts on index page
    blog_home = Post.objects.all().filter(
        status=1).order_by('-updated_on')[:3]

    context = {
        'blog_home': blog_home,
    }

    return render(request, 'home/index.html', context)
