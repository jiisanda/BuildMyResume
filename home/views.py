from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def profileTabView(request):
    return render(request, 'home/portfolio.html')

def blogTabView(request):
    return render(request, 'home/blog.html')

def contactTabView(request):
    return render(request, 'home/contact.html')
