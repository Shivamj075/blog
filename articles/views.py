from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article

def home(request):
	context={
		"Article": Article.objects.all()
	}
	return render(request,"articles/home.html",context)
	# model = Article
	# template_name = 'home.html'

def detail(request,article_id):
	details1 = Article.objects.get(pk=article_id)
	context={
		"details": details1
	}
	return render(request,"articles/detail.html",context)
    # model = Article
    # template_name = 'detail.html'
