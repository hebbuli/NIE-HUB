from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"),
	path('login', views.login, name="login"),
	path('signup',views.signup, name="signup"),
	path('main',views.main,name='main'),
	path('logout', views.logout_view, name = "logout"),
	path('myprofile',views.myprofile,name="myprofile"),
	path('mybooks',views.mybooks,name="mybooks"),
	path('myevents',views.myevents,name="myevents"),
	path('myposts',views.myposts,name="myposts"),
	path('change',views.change,name="change"),
	path('changed',views.changed,name="changed"),
]