from django.contrib import admin
from .models import Product,Category
# Register your models here.


class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,categoryadmin)



class productadmin(admin.ModelAdmin):
    list_display = ['name','available','price','category','image','stock','updated','created']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','available','stock']
    list_per_page = 20

admin.site.register(Product,productadmin)