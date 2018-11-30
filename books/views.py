from django.shortcuts import render,redirect
from nie_hub.models import User
from .models import *
from django.http import HttpResponse
from django.utils import timezone
from django.db import connection

# Create your views here.
def sell(request):
	if request.method == 'POST':
		# uid = User.objects.get(usn = request.session['usn'])
		# books=Books()
		# books.branch= request.POST.get('branch')
		# books.sem= request.POST.get('sem')
		# books.title = request.POST.get('title').upper()
		# books.author= request.POST.get('author').upper()
		# books.save()
		# bid=Books.objects.get(book_id=books.book_id)
		# book_details=Book_details()
		# book_details.edition= request.POST.get('edition')
		# book_details.price= request.POST.get('price')
		# book_details.book_id=bid
		# book_details.owner_id=uid
		# book_details.save()
		user = User.objects.get(usn = request.session['usn'])

		branch= request.POST.get('branch')
		sem= request.POST.get('sem')
		title = request.POST.get('title').upper()
		author= request.POST.get('author').upper()
		
		edition= request.POST.get('edition')
		price= request.POST.get('price')
		owner_id=user.uid

		cursor = connection.cursor()
		cursor.callproc('sell',[branch,sem,title,author,edition,price,owner_id])

		return redirect("main")
	else: 
		return render(request,"books/sell.html", {})

def buy(request): 
    return render(request,'books/buy.html', {})

def buy1(request): 
    return render(request,'books/buy1.html', {})

def buyd(request):
	if request.method == 'POST':
		uid = User.objects.get(usn = request.session['usn'])
		a = request.POST.get('title').upper()
		b = request.POST.get('author').upper()
		c = request.POST.get('edition')
		bid=Books.objects.filter(title=a,author=b)
		bdid=Book_details.objects.filter(edition=c,book_id__in=bid,status=1).exclude(owner_id=uid).order_by("price") 
		length=len(bdid) 
		return render(request,"books/buyd.html",{"bdid":bdid,"length":length,"a":a,"b":b,"c":c,"uid":uid})

def buys(request):
	if request.method == 'POST':
		uid = User.objects.get(usn = request.session['usn'])
		c = request.POST.get('sem')
		d = request.POST.get('branch')
		bid=Books.objects.filter(sem=c,branch=d)
		bdid=Book_details.objects.filter(book_id__in=bid,status=1).exclude(owner_id=uid).order_by("price") 
		length=len(bdid) 
		return render(request,"books/buys.html",{"bdid":bdid,"length":length,"uid":uid})

def waiting_books(request):  
	if request.method == 'POST':
		for key,value in request.POST.items():
			if key[:6]=="submit":
				k=int(key[6:])
		uid = User.objects.get(usn = request.session['usn'])
		bdid = Book_details.objects.get(book_details_id=k)
		if bdid.status == 1:
			waiting_books=Waiting_books()
			waiting_books.date=timezone.now()
			waiting_books.book_details_id=bdid
			waiting_books.buyer_id=uid
			waiting_books.save()
			# bdid.status=0
			# bdid.save()
			return render(request,"books/booked.html")
		else:
			return render(request,"books/missed.html")
		
	else:
		uid = User.objects.get(usn = request.session['usn'])
		wid = Waiting_books.objects.filter(buyer_id=uid).order_by("date")
		# bdid= Book_details.objects.filter(book_details_id=wid.book_details_id)
		# bid= Books.objects.filter(book_id=bdid.book_id)
		length=len(wid)
		bdid1= Book_details.objects.filter(owner_id=uid)
		wid1 = Waiting_books.objects.filter(book_details_id__in=bdid1).order_by("date")
		# bid1= Books.objects.filter(book_id=bdid1.book_id)
		length1=len(wid1)
		return render(request,"books/waiting_books.html",{"wid":wid,"length":length,"wid1":wid1,"length1":length1})

def transaction_books(request):  
	if request.method == 'POST': 
		for key,value in request.POST.items():
			if key[:6]=="submit":
				k=int(key[6:])
		uid = User.objects.get(usn = request.session['usn'])
		if request.POST.get('submit' + str(k))=="Transaction done":
			bdid=Book_details.objects.get(book_details_id=k)
			bid=Books.objects.get(book_id=bdid.book_id.book_id)
			wid=Waiting_books.objects.get(book_details_id=bdid)
			transaction_books=Transaction_books()
			transaction_books.date=timezone.now()
			transaction_books.title1=wid.book_details_id.book_id.title
			transaction_books.author1=wid.book_details_id.book_id.author
			transaction_books.edition1=wid.book_details_id.edition
			transaction_books.price1=wid.book_details_id.price
			transaction_books.owner_id1=wid.book_details_id.owner_id
			transaction_books.buyer_id1=wid.buyer_id
			transaction_books.save()
			bid.delete()
			# bdid.save()
			wid.delete()
			return redirect("main")
			# wid.save()

		else:
			bdid=Book_details.objects.get(book_details_id=k)
			wid=Waiting_books.objects.get(book_details_id=bdid).delete()
			# wid.save()
			bdid.status=1
			bdid.save()
			return redirect("main")


	# uid = User.objects.get(usn = request.session['usn'])
	# transaction_books=Transaction_books()
	# transaction_books.date=timezone.now()
	# transaction_books.buyer_id=uid
	# transaction_books.book_details_id=pk
	# transaction_books.save()
	else:
		uid = User.objects.get(usn = request.session['usn'])
		tid = Transaction_books.objects.filter(buyer_id1=uid).order_by("-date")
		length = len(tid)
		tid1 = Transaction_books.objects.filter(owner_id1=uid).order_by("-date")
		length1 = len(tid1)
		return render(request,"books/transaction_books.html",{"tid":tid,"length":length,"tid1":tid1,"length1":length1})



