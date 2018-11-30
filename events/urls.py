from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('create1',views.create1, name="create1"),
	path('create2/<int:pk>/',views.create2, name="create2"),
	path('create3/<int:pk>/',views.create3, name="create3"),
	path('manage', views.manage, name="manage"),
	path('event_view',views.event_view, name="event_view"),
	path('<int:pk>/',views.event_detail_view,name="event_detail_view"),	
	path('booked_items',views.booked_items, name="booked_items"),
]