from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post
from .forms import ResourceForm
from .models import Resources
import os
from django.conf import settings
# Create your views here.




def home (request):
    posts = Post.objects.all().order_by('-created_at')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/home.html", {"posts":posts})

def show_resource(request):

    resources = Resources.objects.all().order_by('-uploaded_at')
    return render(request,"main/resource.html",{"resources":resources})
    
def map(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/map.html")
    
def history(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/history.html")


def not_found(request, exception):
    response = render(request, 'main/404.html')
    response.status_code = 404
    return response

@login_required(login_url="/anhs")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    return render(request,"main/create_post.html", {"form":form})


def library(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/library.html")
def upload_view(request):
    if request.method=='POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.author = request.user
            file.save()
            return redirect("/library")

        
def download_file(request,filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    with open(file_path,'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file_path))
        
        # Return the response
        return response