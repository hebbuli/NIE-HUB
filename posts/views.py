from django.shortcuts import render,redirect
from .models import Posts,Attachments
from nie_hub.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def create_post(request):
	if request.session.get('usn') != None:
		if request.method == "POST":
			uid = User.objects.get(usn = request.session['usn'])
			
			title = request.POST.get('title')
			branch = request.POST.get('branch')
			sem = request.POST.get('sem')
			body = request.POST.get('body')
			post = Posts.objects.create(title=title, branch = branch, date = timezone.now(), sem = sem, body = body, user_id = uid)
			print(request.FILES.get('attach1'))
			for key,file in request.FILES.items():
				fss = FileSystemStorage()
				fss.save(file.name,file)
				Attachments.objects.create(attachment_link = file, post_id = post)
				
			return redirect("main")	
		else:
			return render(request,'posts/create_post.html',{})
	else:
		return HttpResponse("<h2>You are not logged in<h2>")		

def view_post(request):
	if request.session.get('usn') != None:
		user = User.objects.get(usn = request.session['usn'])
		all_posts = Posts.objects.filter(sem = user.sem, branch = user.branch).order_by("-date")
		length = len(all_posts)
		return render(request,'posts/view_post.html',{'all_posts':all_posts, 'length':length})
	else:
		return HttpResponse("<h2>You are not logged in<h2>")
			
def view_detail(request,pk):
	if request.session.get('usn') != None:
		post = Posts.objects.get(post_id = pk)
		all_attachments = Attachments.objects.filter(post_id= post)
		return render(request,'posts/post_detail.html',{'post':post,'attachments':all_attachments})
	else:
		return HttpResponse("<h2>You are not logged in<h2>")