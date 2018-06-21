from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog
def allblogs(request):
    allblogs = Blog.objects
    return render(request,'blog/home.html',{'blogs':allblogs})

def details(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/details.html',{'blog':detailblog})
