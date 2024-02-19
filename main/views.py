from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Comment
from .forms import ResourceForm, CommentForm
from .models import Resources, Forum
import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Resources
import os
from django.conf import settings

# Create your views here.



@login_required(login_url="/anhs")
def home (request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"main/home.html", {"posts":posts})

@login_required(login_url="/login")
def forum(request):
    forums = Forum.objects.all().order_by('-uploaded_at')
    return render(request,"main/forum.html",{"forums":forums} )

@login_required(login_url="/login")
def show_resource(request,grade,subject):
    resources = Resources.objects.filter(grade=grade,subject=subject, is_approved=True).order_by('-uploaded_at')
    return render(request,"main/resource.html",{"resources":resources,"subject":subject,"grade":grade,})

@login_required(login_url="/login")
def forum_comment(request, id):
    forums = Forum.objects.filter(id=id)
    forum_instance = Forum.objects.get(id=id)
    comments = forum_instance.comments.all().order_by('-uploaded_at')  
    return render(request,"main/forum_about.html",{"forums":forums,"comments":comments})

@login_required(login_url="/login")
def map(request):
    return render(request,"main/map.html")
    
@login_required(login_url="/login")
def history(request):
    return render(request,"main/history.html")

@login_required(login_url="/anhs")
def library(request):
    return render(request,"main/library.html")


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

@login_required(login_url="/anhs")
def comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            id = request.POST.get("id")
            
            comment = form.save(commit=False)
            comment.forum = Forum.objects.get(id=id)
            comment.author = request.user
            comment.save()
            return redirect(f"/forum/{id}")
        else:
            return redirect("/library")
    else:
        form = CommentForm()
    return render(request,"main/forum.html",{"form":form})
def upload_view(request):
    if request.method=='POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.author = request.user
            file.save()
            return redirect("/library")

        
            
def download(request,uuid):
   resource = get_object_or_404(Resources, uuid=uuid)
   file_path = os.path.join(settings.MEDIA_ROOT, resource.file.name)

   if os.path.exists(file_path):
        # Serve the file for downloading
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
   else:
        # Return 404 if the file does not exist
        raise Http404("File does not exist")

        
