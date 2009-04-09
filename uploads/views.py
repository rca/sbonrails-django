from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from uploads.forms import FileForm
from uploads.models import File

@login_required
def form(request):
    if request.method == 'POST':
        file = File()
        file.user = request.user

        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FileForm()

    ctx = {
        'form': form,
        }

    return render_to_response('uploads/form.html', ctx)

def get(request, download_key):
    pass

@login_required
def index(request):
    file_list = File.objects.filter(user=request.user)
    ctx = {
        'file_list': file_list,
        }
    return render_to_response('uploads/index.html', ctx)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def show(request, id):
    pass
