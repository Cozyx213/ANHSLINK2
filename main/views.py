from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Comment
from .forms import ResourceForm, CommentForm, ForumForm
from .models import Resources, Forum
import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Resources
import time
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.serializers import serialize
# Create your views here.



@login_required(login_url="/anhs")
def home (request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"main/home.html", {"posts":posts})

@login_required(login_url="/anhs")
def fetch (request):
    posts = Post.objects.all().order_by('-created_at')
    posts_json = serialize('json', posts)
    return  JsonResponse({"posts":posts_json})



@login_required(login_url="/login")
def show_resource(request,grade,subject):
    resources = Resources.objects.filter(grade=grade,subject=subject, is_approved=True).order_by('-uploaded_at')
    return render(request,"main/resource.html",{"resources":resources,"subject":subject,"grade":grade,})

@login_required(login_url="/login")
def forum_comment(request, id):
    forums = Forum.objects.filter(id=id)
    return render(request,"main/forum_about.html",{"forums":forums})
    
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

@login_required(login_url="/login")
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


@login_required(login_url="/login")
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


@login_required(login_url="/login")
def reply(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            id = request.POST.get("comment_id")
            fid =request.POST.get("fid")
            comment = form.save(commit=False)
            comment.parent = Comment.objects.get(id=id)
            
            comment.author = request.user
            comment.save()
            return redirect(f"/forum/{fid}")
        else:
            return redirect("/library")
    else:
        form = CommentForm()
    return render(request,"main/forum.html",{"form":form})



@login_required(login_url="/login")
def forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.author = request.user
            forum.save()
            return redirect("/forum")
    else:
        form = PostForm()
        
    forums = Forum.objects.all().order_by('-uploaded_at')
    return render(request,"main/forum.html",{
        "forums":forums,
        "form":form,
        "user":request.user.profile
        } )
    
@login_required(login_url="/login")
def get_forums(request):
    start = int(request.GET.get("index") or 0)
    
    forumList =[]
    for i in range(10):
        
        forum = Forum.objects.all().order_by('-uploaded_at')[start:start+i]
        forumList.append(forum)
    form_json = serialize('json', forum)
    return JsonResponse({"forums":form_json})
    


    
@login_required(login_url="/login")
def create_forum(request):
    form = ForumForm(request.POST or None)  # Initialize form for both GET and POST requests
    if request.method == 'POST':
        form_timestamp = request.POST.get('form_timestamp')
        if form_timestamp != request.session.get('last_form_timestamp'):
            request.session['last_form_timestamp'] = form_timestamp
            if form.is_valid():
                forum = form.save(commit=False)
                forum.author = request.user
                forum.save()
                return redirect("/forum")
        else:
            # Redirect or display a message for duplicate submission
            return redirect("/home")  # Example redirect, adjust as needed
    else:
        form_timestamp = str(time.time())
    return render(request, 'my_template.html', {'form': form, 'form_timestamp': form_timestamp})

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

        
