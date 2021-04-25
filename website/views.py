from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseNotFound

from website.models import StoredFile

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

@login_required
def files_view(request):
    files = StoredFile.objects.all()
    context = {
        "files": files,
    }
    return render(request, 'website/files.html', context=context)

@login_required
def file_view(request, filename):
    files = list(StoredFile.objects.filter(file=f"files/{filename}"))

    if len(files) == 0:
        return HttpResponseNotFound(f"<h1>File not found: {filename}</h1>")
    file = files[0]
    return FileResponse(open(file.path(), "rb"))
