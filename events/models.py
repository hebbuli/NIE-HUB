from django.db import models
from nie_hub.models import User

# Create your models here.

class Events(models.Model):
	event_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 40)
	body = models.TextField(null = True,blank=True)
	event_date = models.DateTimeField(null= True)
	create_date = models.DateTimeField(null= True)
	venue = models.CharField(max_length=30,null=True)
	owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Items(models.Model):
	item_id= models.AutoField(primary_key = True)
	category=models.CharField(max_length=30,choices=(("Shirts","Shirts"),("Trousers","Trousers"),("Caps","Caps"),("Others","Others")))
	name=models.CharField(max_length=30,null=True)
	event_id=models.ForeignKey(Events,on_delete=models.CASCADE)

class Item_details(models.Model):
	item_details_id= models.AutoField(primary_key = True)
	size =  models.CharField(max_length=3,null = True)
	quantity=models.IntegerField()
	price=models.IntegerField()
	item_id=models.ForeignKey(Items,on_delete=models.CASCADE)

class Transaction_items(models.Model):
	item_trans_id=models.AutoField(primary_key = True)
	date=models.DateTimeField(null= True)
	quantity_sold = models.IntegerField()
	size =  models.CharField(max_length=3,null = True)
	price=models.IntegerField()
	category= models.CharField(max_length=30,choices=(("Shirts","Shirts"),("Trousers","Trousers"),("Caps","Caps"),("Others","Others")))
	name=models.CharField(max_length=30,null=True)
	owner_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'owner_id') 
	buyer_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'buyer_id')

class Waiting_items(models.Model):
	item_waiting_id=models.AutoField(primary_key = True)
	request_quantity = models.IntegerField()
	date=models.DateTimeField(null= True)
	item_details_id=models.ForeignKey(Item_details,on_delete=models.CASCADE)
	buyer_id=models.ForeignKey(User,on_delete=models.CASCADE)	