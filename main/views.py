from django.shortcuts import render, redirect

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

def login(request):
    return render(request, 'main/login.html', {})