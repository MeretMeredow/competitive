from django.shortcuts import render

def home(request):
    return render(request,'index.html') 

def group(request):
    return render(request, 'group.html')

def emin(request):
    return render(request, 'emin.html')

