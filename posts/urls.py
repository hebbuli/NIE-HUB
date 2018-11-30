from . import views
from django.views.generic import DetailView
from posts.models import Posts
from django.urls import path
from django.conf.urls import url

urlpatterns=[
	path('new',views.create_post ,name="newPost"),
	path('view',views.view_post,name = "viewPost"),
	path('<int:pk>/', views.view_detail, name = "view_detail"),
 ]