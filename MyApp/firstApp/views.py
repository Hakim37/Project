from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {"content": "Welcome to our web portal, this is our landing page!"}
    return render(request, "home_page.html", context)

def login_page(request):
    return render(request, "login_page.html", {})

def contect_page(request):
    return render(request, "contect_page.html", {})
