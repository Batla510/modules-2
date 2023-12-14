from django.shortcuts import render,redirect
from .models import Posts,Category

def index(request):
    posts = Posts.objects.all()
    return render(request,'posts/posts.html',context={'posts':posts})
def delete(request,id):
    try:
        post = Posts.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return redirect('home')
def post(request,id):
    try:
        post = Posts.objects.get(id=id)
        return render(request, 'posts/post.html', context={'post': post})
    except:
        return redirect('home')
def create(request):
    posts = Posts(title='',text='',category_id=1,is_published=True)
    if request.method == 'POST':
        posts.title = request.POST.get('title')
        posts.text = request.POST.get('text')
        posts.category_id = request.POST.get('category')
        posts.is_published = request.POST.get('is_published')
        posts.save()
        return redirect('home')
    else:
        return render(request,'posts/create.html',context={'form':form})
def update(request,id):
    try:
        posts = Posts.objects.get(id=id)
        if request.method == 'POST':
            posts.title = request.POST.get('title')
            posts.text = request.POST.get('text')
            posts.category_id = request.POST.get('category')
            posts.is_published = request.POST.get('is_published')
            posts.save()
            return redirect('home')
        else:
            categories = Category.objects.all()
            return render(request,'posts/update.html',context={'categories': categories,'posts':posts})
    except:
        return redirect('create')
