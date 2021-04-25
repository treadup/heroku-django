from django.shortcuts import redirect, render
from django.contrib.auth import logout

def index_view(request):
    return render(request, "website/index.html")

def logout_view(request):
    logout(request)
    return redirect("index")
