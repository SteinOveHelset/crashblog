from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')