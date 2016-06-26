from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'overseer/index.html', context)
