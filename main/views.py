from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Comment, Subject, Grade, Subject
from .forms import ResourceForm, CommentForm, ForumForm
from .models import Resources, Forum, Classroom
import os
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from .models import Resources
import time
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.conf import settings
from django.core.serializers import serialize
from .serializers import ForumSerializer, PostSerializer, ClassroomSerializer, CommentSerializer, SubjectSerializer
from rest_framework.renderers import JSONRenderer
from authentication.models import Profile

# Create your views here.

def subjects(request):
    grade = Subject.objects.all()
    serializer = SubjectSerializer(grade, many=True)
    return JsonResponse({"subjects":serializer.data})

@login_required(login_url="/anhs")
def home (request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"main/home.html", {"posts":posts})


def fetch (request):
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    
    return  JsonResponse({"posts":serializer.data})

@login_required(login_url="/login")
def forumLogs(request):
    user  = request.user
    profile = Profile.objects.get(user=user.id)
    posts = Forum.objects.filter(author=profile.id).order_by('-uploaded_at')
    
    serialized = ForumSerializer(posts,many=True)
    
    return JsonResponse({"posts": serialized.data})


def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    
    return render(request, 'registration/post_detail.html',{'post':post})

@login_required(login_url="/login")
def commentLogs(request):
    user  = request.user
    profile = Profile.objects.get(user=user.id)
    comments = Comment.objects.filter(author=profile.id).order_by('-uploaded_at')
    
    serialized = CommentSerializer(comments,many=True)
    
    return JsonResponse({"posts": serialized.data})


@login_required(login_url="/login")
def show_resource(request,grade,subject):
    grade = int(grade)-6
    subject = Subject.objects.get(grade = grade, name=subject)
    
    resources = Resources.objects.filter(grade=grade,subject=subject, is_approved=True).order_by('-uploaded_at')
    return render(request,"main/resource.html",{"resources":resources,"subject":subject,"grade":grade})

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
            comment.author =  Profile.objects.get(user=request.user)
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
            
     
            user_profile = Profile.objects.get(user=request.user)
            
            id = request.POST.get("comment_id")
            fid =request.POST.get("fid")
            
            comment = form.save(commit=False)
            
            comment.author =  user_profile
            comment.parent = Comment.objects.get(id=id)
            
           
            
            comment.save()
            return redirect(f"/forum/{fid}")
        else:
            return redirect("/library")
    else:
        form = CommentForm()
    return render(request,"main/forum.html",{"form":form})



@login_required(login_url="/login")
def forum(request):
    form = "blew"
    if request.method == 'POST':
       new_forum = Forum(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            # ... other fields ...
        )  
        # Assuming that there is a one-to-one relationship between User and Profile
       try:
           user_profile = Profile.objects.get(user=request.user)
           new_forum.author = user_profile
       except Profile.DoesNotExist:
           # Handle the case where the Profile does not exist for the User
           # You might want to create a Profile instance or return an error
           pass
        
       new_forum.save()
       return redirect(f"/forum/{new_forum.id}")
    else:
        form = PostForm()
        user_profile= None
        try:
            user_profile = request.user
        except Profile.DoesNotExist:
            return render(request,"/sign_up")
        
    return render(request,"main/forum.html",{
       "form":form,
        "user":request.user.profile
        } )
    
@login_required(login_url="/login")
def get_forums(request):
    start = int(request.GET.get("index") or 0)
    
   
    forums = Forum.objects.all().order_by('-uploaded_at')[start:start+10]
    
    serializer = ForumSerializer(forums, many=True)
    return JsonResponse({"forums": serializer.data})
   #return JsonResponse({"forums":form_json})
    
@login_required(login_url="/login")
def room(request):
    rooms = Classroom.objects.all()
    serializedRoom = ClassroomSerializer(rooms, many =True)
    return JsonResponse({"rooms":serializedRoom.data})

    

def upload_view(request):
    if request.method=='POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.author = request.user
            file.name = request.FILES['file'].name
            file.save()
            return redirect("/library")

        
@login_required(login_url="/login")
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



@login_required(login_url="/login")
def classroom(request):
    return render(request,"main/classroom.html")

@login_required(login_url="/login")
def logs_view(request):
    return render(request,"main/logs.html")



@login_required(login_url="/login")
def deleteForum(request, forumID):
    if request.method == "DELETE":
        try:
            forum = Forum.objects.get(id = forumID)
            forum.delete()
            return JsonResponse({"mesasge": "message deleted"})
        except Forum.DoesNotExist:
            return JsonResponse({"error": "Forum not found"})
    else:
        return HttpResponseNotAllowed(['DELETE'])

@login_required(login_url="/login")
def deleteComment(request, commentID):
    if request.method == "DELETE":
        try:
            comment = Comment.objects.get(id = commentID)
            comment.delete()
            return JsonResponse({"mesasge": "message deleted"})
        except Forum.DoesNotExist:
            return JsonResponse({"error": "Comment  not found"})
    else:
        return HttpResponseNotAllowed(['DELETE'])

