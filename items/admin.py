

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(ProductPhoto)