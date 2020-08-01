from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Comment
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def list(request):
    blogs=Blog.objects
    return render(request,'list.html',{'blogs':blogs})

def detail(request,blog_id) :
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_object})

def create(request) :
    return render(request, 'create.html')

def new(request) :
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.ow()
    blog.save()

    return redirect('/blog/' +str(blog.id))

def delete(request):
    blogs = Blog.objects.get(pk= blog_id)
    blogs.delete()
    return redirect('list')

def edit(request, blog_id):
    blog_edit = Blog.objects.get(pk=blog_id)
    return render(request, 'edit.html',{'blog':blog_edit})

def home(request):
    comment=Comment.objects
    return render(request, 'home.html')


@csrf_exempt
def update(request, blog_id) :
    blog = Blog.objects.get(pk-blog_id)
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('home')