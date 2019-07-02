from django.contrib import admin

# Register your models here.
from dzdp.models import DzdpType, DzdpCity, DzdpShop, DzdpCityType, DzdpShopType

admin.site.register(DzdpCity)
admin.site.register(DzdpType)
admin.site.register(DzdpCityType)
admin.site.register(DzdpShop)
admin.site.register(DzdpShopType)
