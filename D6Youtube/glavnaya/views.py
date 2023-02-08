from django.shortcuts import render


def index(request):
    return render(request, 'glavnaya/index.html')


def about(request):
    return render(request, 'glavnaya/about.html')
