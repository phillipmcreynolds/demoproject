from django.contrib import admin

# Register your models here.
from .models import Drinks
from .models import Menu
from .models import MenuCategory
from .models import Booking

admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Booking)