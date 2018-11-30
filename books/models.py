from django.db import models
from nie_hub.models import User

# Create your models here.

class Books(models.Model):
	book_id = models.AutoField(primary_key = True)
	branch = models.CharField(max_length = 3,choices= (('CE','CE'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('ISE','ISE'),('ME','ME'),('IPE','IPE')))
	sem = models.IntegerField(null = False, choices= ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
	title= models.CharField(max_length=50)
	author= models.CharField(max_length=30)

class Book_details(models.Model):
	book_details_id= models.AutoField(primary_key = True)
	edition=models.IntegerField()
	price=models.IntegerField()
	status=models.IntegerField(default=1)
	book_id=models.ForeignKey(Books,on_delete=models.CASCADE)
	owner_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Waiting_books(models.Model):
	book_wait_id=models.AutoField(primary_key = True)
	date=models.DateTimeField(null= True)
	book_details_id=models.ForeignKey(Book_details,on_delete=models.CASCADE)
	buyer_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Transaction_books(models.Model):
	book_trans_id=models.AutoField(primary_key = True)
	date=models.DateTimeField(null= True)
	title1= models.CharField(max_length=60,null=True)
	author1= models.CharField(max_length=30,null=True)
	edition1=models.IntegerField(null=True)
	price1=models.IntegerField(null=True)
	owner_id1 = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'owner_id1') 
	buyer_id1 = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'buyer_id1')
