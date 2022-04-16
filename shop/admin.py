from django.contrib import admin

# Register your models here.

from .models import Product , Stores, Contact, Signup, Orders ,OrderUpdate

admin.site.register(Product)

admin.site.register(Stores)

admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
