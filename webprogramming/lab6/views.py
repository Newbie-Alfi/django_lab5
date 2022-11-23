from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.
def home(request):
    article = Article.objects.all()
    context  = {
        'articles': article
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def show_article():
    article = get_object_or_404(Article)