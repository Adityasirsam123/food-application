from django.contrib import admin
from foodapp.models import Food, Cust, Admin, Cart, Order,Restaurant
from .models import Food
class FoodAdmin(admin.ModelAdmin):
    list_display = ('FoodName', 'Description', 'FoodCat', 'FoodPrice', 'FoodImage')
    list_filter = ['FoodCat']  # Filter by category and restaurant
    search_fields = ('FoodName', 'FoodCat')  # Search by restaurant name
    ordering = ('FoodName',)

# Register the models with the admin site
admin.site.register(Food, FoodAdmin)
admin.site.register(Cust)
admin.site.register(Admin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Restaurant)
