from django.shortcuts import render

# Create your views here.
def list(request):
    blogs=Blog.objects
    return render(request,'list.html',{'blogs':blogs})