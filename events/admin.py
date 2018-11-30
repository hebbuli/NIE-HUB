from django.contrib import admin
from .models import Events,Items,Item_details,Transaction_items,Waiting_items

# Register your models here.
admin.site.register(Events)
admin.site.register(Items)
admin.site.register(Item_details)
admin.site.register(Transaction_items)
admin.site.register(Waiting_items)