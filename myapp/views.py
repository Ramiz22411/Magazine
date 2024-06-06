from django.shortcuts import render


# Create your views here.

def index(request):
    template = 'myapp/index.html'
    context = {
    }
    return render(request, template, context)


def about(request):
    template = 'myapp/about.html'
    context = {
    }
    return render(request, template, context)
