from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    return render(request, 'home.html', {})

def signUp(request):
    return render(request, 'signup.html', {})

def logIn(request):
    return render(request, 'login.html', {})

def post(request):
    return render(request, 'post.html', {})

def loggedIn(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    address = request.POST.get('address')
    picode = request.POST.get('code')
    gender = request.POST.get('optradio')
    mail = request.POST.get('email')
    password = request.POST.get('password')
    if name is None or age is None or address is None or picode is None or gender is None or mail is None or password is None:
        return HttpResponse('register not complete')
    else:
        return render(request, 'loggedin.html', {"name":name})

def loggedHome(request):
    return render(request, 'loggedhome.html', {})
        
def anBuLa(request):
    return redirect("https://blog.ipleaders.in/anti-bullying-laws/")

def women(request):
    return redirect("https://edugeneral.org/blog/polity/women-rights-in-india/")

def everyone(request):
    return redirect("https://en.wikipedia.org/wiki/National_Human_Rights_Commission_of_India")

def child(request):
    return redirect("https://www.cry.org/child-rights")