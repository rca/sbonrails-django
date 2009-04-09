from django.http import HttpResponse
from django.shortcuts import render_to_response

from uploads.models import File

def form(request):
    pass

def get(request, download_key):
    pass

def index(request):
    file_list = File.objects.filter(user=request.user)
    ctx = {
        'file_list': file_list,
        }
    return render_to_response('uploads/index.html', ctx)

def show(request, id):
    pass
