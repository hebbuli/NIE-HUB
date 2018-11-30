from django.shortcuts import render,redirect,get_object_or_404
from nie_hub.models import User
from .models import Events,Items,Item_details,Transaction_items,Waiting_items
from django.utils import timezone 
from django.db.models import F

# Create your views here.
def create1(request):
      if request.session.get('usn') != None:
            if request.method == 'POST':
                  uid = User.objects.get(usn = request.session['usn'])
                  events=Events()
                  submit_type = request.POST.get('submit')
                  events.name = request.POST.get('ename')
                  events.body= request.POST.get('body')
                  events.event_date= request.POST.get('edate')
                  events.venue= request.POST.get('venue')
                  events.create_date=timezone.now()
                  events.owner_id= uid
                  events.save()
                  url = "create2/"+str(events.event_id)
                  if( submit_type == "NEXT"):
                        return redirect(url)
                  else:
                        return redirect("main")      
            else:
                  return render(request,"events/create_event1.html", {})
      else:
          return HttpResponse("<h2>You are not logged in<h2>")              

def create2(request,pk):
      if request.session.get('usn') != None:
            if request.method == "POST":
                  event = Events.objects.get(event_id = pk)
                  type_count = int(request.POST.get('types'))
                  iname=[]
                  category = []
                  for i in range(type_count):
                        item_name = 'iname' + (str(i))
                        category_name = 'category' + (str(i))
                        iname.append(request.POST.get(item_name))
                        category.append(request.POST.get(category_name))

                  for i in range(len(iname)):
                        item_object = Items.objects.create(category=category[i],name = iname[i],event_id = event)
                  url = "/events/create3/"+ str(pk)
                  return redirect(url)
            else:
                  return render(request,"events/create_event2.html",{})
      else:
          return HttpResponse("<h2>You are not logged in<h2>")              

def create3(request,pk):
      if request.session.get('usn') != None:
            if request.method == "POST":
                  length = Items.objects.filter(event_id = pk).count()
                  for i in range(length):
                        check_type = "type" + str(i)
                        item_name = "item"+ str(i)
                        item_id = request.POST.get(item_name)
                        item = Items.objects.get(item_id= item_id)
                        if request.POST.get(check_type) == None:
                              quantity_name = "quantity"+ str(i)
                              price_name = 'price'+ str(i)
                              quantity = request.POST.get(quantity_name)
                              price = request.POST.get(price_name)
                              Item_details.objects.create(size= None,quantity= quantity,price = price,item_id= item)
                        else:        
                              quantity_size_list1 = ['quantity-XXS','quantity-XS','quantity-S','quantity-M','quantity-L','quantity-XL','quantity-XXL','quantity-O']
                              price_size_list1 = ['price-XXS','price-XS','price-S','price-M','price-L','price-XL','price-XXL','price-O']
                              string = str(i)
                              quantity_size_list = [s + string for s in quantity_size_list1]
                              price_size_list = [s +  string for s in price_size_list1]
                              for j in range(len(quantity_size_list)):
                                    qty = request.POST.get(quantity_size_list[j])      
                                    if qty!= '' and qty!= None:
                                          size = quantity_size_list[j][9:len(quantity_size_list1[j])]
                                          price = request.POST.get(price_size_list[j])
                                          qty = int(qty)
                                          price = int(price)
                                          Item_details.objects.create(size= size,quantity= qty,price = price,item_id= item)

                  return render(request,"events/event_success.html")
            else:
                  all_items = Items.objects.filter(event_id = pk)
                  return render(request,"events/create_event3.html",{'all_items':all_items})
      else:
          return HttpResponse("<h2>You are not logged in<h2>")    

def event_view(request):  
      if request.session.get('usn') != None:
            user = request.session.get('usn');
            user_id = User.objects.get(usn = user)
            all_data = Events.objects.all().exclude(owner_id = user_id).order_by("-event_date")
            past_events = all_data.filter(event_date__lt = timezone.now())
            upcoming_events = all_data.filter(event_date__gte = timezone.now())
            return render(request,'events/event_view.html',{'upcoming_events':upcoming_events,'past_events':past_events,'length_u':len(upcoming_events),'length_p':past_events})
      else:
            return HttpResponse("<h2>You are not logged in<h2>")                        


def event_detail_view(request,pk):
      if request.session.get('usn') != None:
            user = User.objects.get(usn = request.session['usn'])
            event = Events.objects.get(event_id = pk)
            items = Items.objects.filter(event_id = event)
            item_details = Item_details.objects.filter(item_id__in = items)
            print(item_details)
            if request.method == "POST":
                  for item in item_details:
                        print("hi")
                        quantity_name = "order-qty"+ str(item.item_details_id)
                        choice_name = 'order-choice' + str(item.item_details_id)
                        if request.POST.get(choice_name)!=None:
                              quantity = request.POST.get(quantity_name)
                              Waiting_items.objects.create(request_quantity = quantity,date = timezone.now(),item_details_id = item,buyer_id = user)
                              
                  return redirect("booked_items")
            else:      
                  return render(request,'events/event_detail_view.html',{'event':event,'items_length': len(items),'item_details':item_details})
      else:
            return HttpResponse("<h2>You are not logged in<h2>")


def manage(request):
      if request.session.get('usn') != None:
            user = User.objects.get(usn = request.session['usn'])
            if request.method == "POST":
                  for key,value in request.POST.items():
                        if key[:6] == "submit":      
                              waiting_item_id = key[6:]
                              print(waiting_item_id)
                              waiting_item_id = int(waiting_item_id)
                              waiting_item = Waiting_items.objects.get(item_waiting_id = waiting_item_id)
                              print(waiting_item.request_quantity)
                              Item_details.objects.filter(item_details_id = waiting_item.item_details_id.item_details_id).update(quantity = F('quantity')- waiting_item.request_quantity)
                              
                              Transaction_items.objects.create(date= timezone.now(),quantity_sold = waiting_item.request_quantity,size = waiting_item.item_details_id.size , buyer_id= waiting_item.buyer_id,price= waiting_item.item_details_id.price ,category= waiting_item.item_details_id.item_id.category,name= waiting_item.item_details_id.item_id.name ,owner_id = waiting_item.item_details_id.item_id.event_id.owner_id)
                              Waiting_items.objects.filter(item_waiting_id = waiting_item.item_waiting_id).delete()
                  return redirect("manage")
            else:   
                  my_waiting_items = []
                  all_waiting_items = Waiting_items.objects.all()
                  for waiting_item in all_waiting_items:
                        if waiting_item.item_details_id.item_id.event_id.owner_id == user:
                              my_waiting_items.append(waiting_item)      
                  return render(request,"events/manage_event.html",{'my_waiting_items':my_waiting_items, 'length': len(my_waiting_items   )})
      else:
            return HttpResponse("<h2>You are not logged in<h2>")            


def booked_items(request):
      if request.session.get('usn') != None:
            user = User.objects.get(usn = request.session['usn'])
            all_items = Waiting_items.objects.filter(buyer_id = user).order_by("-date")
            return render(request,'events/booked_items.html',{'all_items':all_items,'length':len(all_items)})
      else:
            return HttpResponse("<h2>You are not logged in<h2>")      