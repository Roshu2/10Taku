from django.shortcuts import render

def first_view(request):
    return render(request, 'animation/detail.html')