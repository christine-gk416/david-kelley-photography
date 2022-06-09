from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Post, Comment
from .forms import CommentForm, PostForm


def blog(request):
    """ A view to show all blog posts and comment count """
    comments = Comment.objects.all()
    posts = Post.objects.all()

    paginator = Paginator(posts, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'comments': comments,
        'page_obj': page_obj,
    }

    return render(request, 'blog/all_posts.html', context)


def post_detail(request, slug):
    """ A view to show individual blog posts by unique url slug """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Blog comment view based on Djano Central guide
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


@login_required
def like_post(request, slug):
    """ Users can like posts if logged in """
    post = get_object_or_404(Post, id=request.POST.get('like_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))


@login_required
def add_post(request):
    """ Add a blog post to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only blog admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save post form but don't commit
            post = form.save(commit=False)
            # Assign author to current user
            post.author = request.user
            # Then save blog post to database
            post.save()
            messages.success(request, 'Successfully added post!')
            # Slugify post title and open new post detail
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request,
                           'Failed to add post.\
                            Please ensure the form is valid.')
    else:
        form = PostForm()

    posts = Post.objects.all()
    template = 'blog/add_post.html'
    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit a blog post  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only blog admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. \
                           Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only blog admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
