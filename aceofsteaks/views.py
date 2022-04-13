from django.shortcuts import render


def index(request):
    """Returns and renders home page."""
    return render(request, 'index.html')


def menu(request):
    """Returns and renders menu page."""
    return render(request, 'menu.html')
