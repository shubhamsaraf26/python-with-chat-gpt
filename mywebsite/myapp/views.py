from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sanity(request):
    return render(request, 'sanity.html')

def health_check(request):
    return render(request, 'health_check.html')

def backup_check(request):
    return render(request, 'backup_check.html')
