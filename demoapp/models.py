from django.db import models
from django.db.models import CharField, IntegerField, DateField

# Create your models here.
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, 
                                    on_delete=models.PROTECT, 
                                    default=None, 
                                    related_name="category_name")
    
class Booking(models.Model):
    first_name = CharField(max_length = 200)
    last_name = CharField(max_length = 200)
    guest_count = IntegerField
    reservation_time = DateField(auto_now = True)
    comments = CharField(max_length = 1000)