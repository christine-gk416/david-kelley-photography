from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def blog(request):
    """ A view to show all products, including sorting and search queries """

    posts = Post.objects.all()
   
    context = {
        'posts': posts,
    }

    return render(request, 'blog/all_posts.html', context)


def post_detail(request, slug):
    # template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

#Blog comment
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
    post = get_object_or_404(Post, id=request.POST.get('like_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    else:
         post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse ('post_detail', args=[str(slug)]))


@login_required
def add_post(request):
    """ Add a blog post to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only blog admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
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
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
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