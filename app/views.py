from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def register(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES["profile"]
            fs = FileSystemStorage()
            saved_file = fs.save(file.name, file)
            file_url = fs.url(saved_file)
        return HttpResponse("success<br><img src='{url}'>".format(file=file, url = file_url))

    return render(request, 'pages/register.html')