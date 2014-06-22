from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from blog.models import Post, Comment
from forms import BlogForm,CommentForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def view_blog(request, id):
    post = Post.objects.filter(id=id)
    if post:
        post = post[0]
    	return render(request, 'blog/view.html', { 'post': post}) 
    else:
        messages.error(request, 'Selected blog doesn\'t exist')
        return redirect('home')

#def view_comment(request):
#    comment = Comment.objects.all()
#    return render(request, 'blog/view.html', {'comment' : comment})



def add_blog(request):
    if 'POST' == request.method:
        form = BlogForm(request.POST)
        if form.is_valid():
            # save the data
            form.save()
            messages.success(request, 'Blog details saved successfully.')
            return redirect('home')
        else:
            # error message 
            messages.error(request, 'Sumbitted form is invalid.')
    else:
        form = BlogForm()
    return render(request, 'blog/form.html', { 'form': form, 'action_title': 'Add Blog'})

def edit_blog(request, id):
    post = Post.objects.filter(id=id)
    if post:
        post = post[0]
        form = BlogForm({
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'content': post.content,
            'slug': post.slug,
            'author': post.author,
            'link': post.link,
            'link_description': post.link_description,
        })
        return render(request, 'blog/form.html', { 'form': form, 'action_title': 'Update Blog'}) 
    else:
        messages.error(request, 'Selected blog doesn\'t exist')
        return redirect('home')

def confirm_blog(request,id):
    post = Post.objects.filter(id=id)
    if post:
        post = post[0]
    return render(request, 'blog/confirm.html', {'post' :post})

def del_blog(request, id):
    post = Post.objects.filter(id=id)
    if post:
        post.delete()
        messages.success(request, 'Blog deleted successfully.')
    else:
        messages.error(request, 'Selected blog doesn\'t exist')
    return redirect('home')

def add_comment(request,id):
    post = Post.objects.filter(id=id)
    if post:
        post = post[0]
        if 'POST' == request.method:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = CommentForm()
        return render(request, 'blog/blogger.html', { 'form' : form , 'post': post} ) 
