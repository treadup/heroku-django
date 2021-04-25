from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def index_view(request):
    return render(request, "website/index.html")

def logout_view(request):
    logout(request)
    return redirect("index")

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        redirect_url = request.GET.get("next", "/")
        if user is not None:
            login(request, user)
            return redirect(redirect_url)

    return render(request, 'website/login.html')
