from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Category, Post, Suscribe

# Create your views here.

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_suscribe = Suscribe()
        new_suscribe.email = email
        new_suscribe.save()

    context = {
        'featured' : featured,
        'latest': latest
    }

    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')
