from django.shortcuts import render
from django.http import HttpResponse
from index.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog(request):
    post_list = Post.objects.all()

    context ={
        'post_list' : post_list,
    }
    return render(request, 'blog.html', context)