from django.shortcuts import render, get_object_or_404,redirect
from .models import Subject,Comment, Hashtag
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .form import CommentForm

# Create your views here.
def subject(request):
    blogs=Subject.objects
    return render(request,'subject.html',{'blogs':blogs})

def detail(request,blog_id) :
    blog_object = get_object_or_404(Subject, pk=blog_id)
    hashtags = blog_object.hashtag.all()
    return render(request, 'detail.html', {'blog' : blog_object, 'hashtags':hashtags})

def create(request) :
    return render(request, 'create.html')

def new(request) :
    blog = Subject()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.professor = request.GET['professor']
    blog.save()

    hashtags=request.GET['hashtags']
    hashtag=hashtags.split(",")
    for tag in hashtag:
        ht = Hashtag()
        ht.name = tag
        ht.save()
        blog.hashtag.add(ht)

    return redirect('/blog/' +str(blog.id))

def delete(request, blog_id):
    blogs = Subject.objects.get(pk= blog_id)
    blogs.delete()
    return redirect('subject')

def edit(request, blog_id):
    blog_edit = Subject.objects.get(pk=blog_id)
    return render(request, 'edit.html',{'blog':blog_edit})

def home(request):
    comment=Comment.objects
    return render(request, 'home.html')


@csrf_exempt
def update(request, blog_id) :
    blog = Subject.objects.get(pk=blog_id)
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('subject')


#댓글
def add_comment_to_post(request, blog_id):
    blog = get_object_or_404(Subject, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('http://127.0.0.1:8000/blog/'+str(blog_id))
    else:
        form = CommentForm()
        return render(request, 'comment.html', {'form':form})