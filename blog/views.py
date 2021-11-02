from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

def blog(request):
    """ A view to show all products, including sorting and search queries """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/all_posts.html', context)


# def post_detail(request, slug):
#     """ A view to show individual product details """

#     post = get_object_or_404(Post, slug = slug)

#     context = {
#         'post': post,
#     }

#     return render(request, 'blog/post_detail.html', context)


#Blog comment

def post_detail(request, slug):
    # template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None


    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()


    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, 'blog/post_detail.html', 
                    context)